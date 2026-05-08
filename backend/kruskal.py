import networkx as nx


def executar_kruskal(G: nx.Graph) -> nx.Graph:
    print("\n" + "═" * 60)
    print("   ALGORITMO DE KRUSKAL — PASSO A PASSO")
    print("═" * 60)
    print(f"  Vértices (cidades):    {G.number_of_nodes()}")
    print(f"  Arestas disponíveis:   {G.number_of_edges()}")
    print("─" * 60)

    arestas_ordenadas = sorted(
        G.edges(data=True), key=lambda x: x[2]["weight"]
    )

    print("\n  [1] Arestas ordenadas por custo (todas):\n")
    for u, v, d in arestas_ordenadas:
        print(f"      {u:22} ↔  {v:22}  {d['weight']:.1f} km")

    mst = nx.minimum_spanning_tree(G, algorithm="kruskal")

    mst_set = set(
        (min(u, v), max(u, v)) for u, v in mst.edges()
    )

    print("\n  [2] Arestas selecionadas para a MST:\n")
    custo_total = 0
    for u, v, d in arestas_ordenadas:
        key = (min(u, v), max(u, v))
        if key in mst_set:
            custo_total += d["weight"]
            print(f" ADICIONADA  {u:22} ↔  {v:22}  {d['weight']:.1f} km")
        else:
            print(f" descartada  {u:22} ↔  {v:22}  {d['weight']:.1f} km  (formaria ciclo)")

    print("\n" + "─" * 60)
    print(f"  Custo total da MST:  {custo_total:.1f} km de cabo")
    print(f"  Conexões usadas:     {mst.number_of_edges()} de {G.number_of_edges()} possíveis")
    print("═" * 60 + "\n")

    return mst