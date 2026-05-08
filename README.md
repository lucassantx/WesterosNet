# WesterosNet

Trabalho prático de Estrutura de Dados — **Grafos**.

Aplicação que resolve o problema de conectar bairros de uma cidade (Aqui interpretados como Reinos de "A Song Of Ice And Fire") com fibra óptica usando o menor comprimento possível de cabo.

## Problema

Dado um conjunto de bairros e as possíveis conexões entre eles (cada uma com um custo em km), encontrar **quais conexões instalar** para que todos os bairros fiquem conectados com o **menor custo total**.

## Modelagem

| Conceito       | Representação no grafo         |
|----------------|-------------------------------|
| Bairro         | Vértice                        |
| Conexão viável | Aresta                         |
| Custo de cabo  | Peso da aresta (km)            |
| Tipo de grafo  | Não-direcionado Ponderado      |

## Algoritmo: Kruskal

1. Ordena todas as arestas pelo peso (menor → maior)
2. Para cada aresta, adiciona à MST **somente se não formar ciclo**
3. Repete até conectar todos os vértices

Detecta ciclos internamente via **Union-Find**.  
Complexidade: **O(E log E)** — E = número de arestas.

## Estrutura do projeto

```
fibranet/
├── backend/
│   ├── __init__.py
│   ├── grafo.py      ← dados: bairros e conexões
│   └── kruskal.py    ← algoritmo + saída no terminal
├── frontend/
│   └── template.html ← interface visual (estilo mapa)
├── main.py           ← orquestrador principal
├── requirements.txt
└── README.md
```

## Como rodar

```bash
pip install -r requirements.txt
python main.py
```

Abre o `output.html` gerado no navegador.

## Resultado esperado

- Terminal: passo a passo do Kruskal, mostrando quais arestas foram aceitas ou descartadas
- `output.html`: visualização interativa do grafo com a MST destacada

## Tecnologias

- Python 3.x
- [NetworkX](https://networkx.org/) — estrutura e algoritmo do grafo
- [Pyvis](https://pyvis.readthedocs.io/) — renderização interativa