import networkx as nx

BAIRROS = [
    "The North",
    "The Vale of Arryn",
    "The Riverlands",
    "The Westerlands",
    "The Crownlands",
    "The Reach",
    "The Stormlands",
    "Dorne",
    "The Iron Islands",
    "Winterfell",
    "King's Landing",
    "Casterly Rock",
    "Highgarden",
    "The Eyrie",
    "Riverrun",
    "Storm's End",
    "Sunspear",
    "Harrenhal",
    "The Wall",
]

CONEXOES = [
    ("The North",        "Winterfell",         2.4),
    ("The North",        "The Wall",            5.8),
    ("The North",        "The Riverlands",      6.1),
    ("The North",        "The Iron Islands",    7.0),
    ("Winterfell",       "The Wall",            3.2),
    ("Winterfell",       "The Riverlands",      4.5),
    ("Winterfell",       "Harrenhal",           5.3),
    ("The Wall",         "The Iron Islands",    8.1),
    ("The Riverlands",   "Harrenhal",           2.8),
    ("The Riverlands",   "Riverrun",            3.0),
    ("The Riverlands",   "The Crownlands",      4.2),
    ("The Riverlands",   "The Westerlands",     5.6),
    ("Harrenhal",        "King's Landing",      3.7),
    ("Harrenhal",        "The Crownlands",      2.9),
    ("Riverrun",         "The Westerlands",     2.6),
    ("Riverrun",         "Casterly Rock",       3.4),
    ("The Westerlands",  "Casterly Rock",       1.9),
    ("The Westerlands",  "The Iron Islands",    6.3),
    ("The Crownlands",   "King's Landing",      1.5),
    ("The Crownlands",   "The Stormlands",      4.8),
    ("The Crownlands",   "The Vale of Arryn",   5.2),
    ("King's Landing",   "The Stormlands",      3.6),
    ("King's Landing",   "The Reach",           5.9),
    ("King's Landing",   "The Vale of Arryn",   4.4),
    ("The Vale of Arryn","The Eyrie",           2.1),
    ("The Vale of Arryn","The Riverlands",      4.7),
    ("The Eyrie",        "Harrenhal",           3.9),
    ("The Reach",        "Highgarden",          2.3),
    ("The Reach",        "The Stormlands",      4.1),
    ("The Reach",        "Dorne",               6.7),
    ("Highgarden",       "Casterly Rock",       5.0),
    ("Highgarden",       "Dorne",               5.5),
    ("The Stormlands",   "Storm's End",         2.7),
    ("The Stormlands",   "Dorne",               5.3),
    ("Storm's End",      "Dorne",               4.6),
    ("Dorne",            "Sunspear",            2.0),
    ("Sunspear",         "The Reach",           7.2),
]


def construir_grafo() -> nx.Graph:
    G = nx.Graph()
    G.add_nodes_from(BAIRROS)
    for origem, destino, custo in CONEXOES:
        G.add_edge(origem, destino, weight=custo)
    return G