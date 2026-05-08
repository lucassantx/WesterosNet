import json
import re
import os
import tempfile
import pathlib

from pyvis.network import Network
from backend.grafo import construir_grafo
from backend.kruskal import executar_kruskal

def gerar_html(G, mst):
    custo_total = sum(d["weight"] for _, _, d in mst.edges(data=True))
    mst_set = set((min(u, v), max(u, v)) for u, v in mst.edges())

    net = Network(height="100%", width="100%", bgcolor="transparent", notebook=False)
    net.set_options(json.dumps({
        "physics": {
            "barnesHut": {
                "gravitationalConstant": -9000,
                "centralGravity": 0.25,
                "springLength": 180,
                "springConstant": 0.035,
                "damping": 0.14
            },
            "stabilization": {"iterations": 250}
        },
        "interaction": {"hover": True, "tooltipDelay": 80}
    }))

    for cidade in G.nodes():
        net.add_node(
            cidade,
            label=cidade,
            color={
                "background": "rgba(0,200,255,0.08)",
                "border": "#00c8ff",
                "highlight": {"background": "rgba(0,200,255,0.2)", "border": "#00e5ff"}
            },
            size=20,
            font={"size": 15, "color": "#cdd8f0", "face": "Rajdhani, sans-serif"},
            borderWidth=2,
            shadow={"enabled": True, "color": "rgba(0,200,255,0.2)", "size": 12}
        )

    for u, v, d in G.edges(data=True):
        key = (min(u, v), max(u, v))
        is_mst = key in mst_set
        net.add_edge(
            u, v,
            label=f"{d['weight']:.1f}",
            color={"color": "#00c8ff" if is_mst else "rgba(80,120,180,0.35)"},
            width=3 if is_mst else 1,
            font={
                "size": 12 if is_mst else 11,
                "color": "#00c8ff" if is_mst else "rgba(80,120,180,0.5)",
                "face": "Share Tech Mono, monospace"
            },
            title=f"{'[MST] ' if is_mst else ''}{u} ↔ {v}: {d['weight']} km",
            dashes=not is_mst,
        )

    _tmp = str(pathlib.Path(tempfile.gettempdir()) / "_pyvis_raw.html")
    net.save_graph(_tmp)
    with open(_tmp, "r", encoding="utf-8") as f:
        raw = f.read()

    body_match = re.search(r'(<div id="mynetwork".*?</script>)', raw, re.DOTALL)
    graph_block = body_match.group(1) if body_match else "<p>Erro ao gerar grafo</p>"

    todas_arestas = []
    for u, v, d in sorted(G.edges(data=True), key=lambda x: x[2]["weight"]):
        key = (min(u, v), max(u, v))
        todas_arestas.append({
            "de": u,
            "para": v,
            "km": round(d["weight"], 1),
            "mst": key in mst_set
        })

    n_mst = mst.number_of_edges()
    n_total = G.number_of_edges()
    n_desc = n_total - n_mst

    with open("frontend/template.html", "r", encoding="utf-8") as f:
        template = f.read()

    todas_json = json.dumps(todas_arestas, ensure_ascii=False).replace("</", "<\\/")

    html = (
        template
        .replace("{{GRAPH_BLOCK}}", graph_block)
        .replace("{{N_BAIRROS}}", str(G.number_of_nodes()))
        .replace("{{N_CONEXOES}}", str(n_total))
        .replace("{{N_MST}}", str(n_mst))
        .replace("{{N_DESCARTADAS}}", str(n_desc))
        .replace("{{CUSTO_TOTAL}}", f"{custo_total:.1f}")
        .replace("{{TODAS_ARESTAS_JSON}}", todas_json)
    )

    output = "output.html"
    with open(output, "w", encoding="utf-8") as f:
        f.write(html)

    print(f" Visualização gerada: {os.path.abspath(output)}")
    print("   Abra o arquivo output.html no navegador.\n")

if __name__ == "__main__":
    G   = construir_grafo()
    mst = executar_kruskal(G)
    gerar_html(G, mst)