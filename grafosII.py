import networkx as nx
import dwave_networkx as dnx
import matplotlib.pyplot as plt
# Resolver el Grafo utilizando el qpu
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
#Crear un grafo de 6 nodos
s5 = nx.star_graph(5)
G=nx.Graph()
G.add_nodes_from(["1","2","3","4","5","6"])
G.add_edge("1","2")
G.add_edge("1","3")
G.add_edge("2","3")
G.add_edge("2","4")
G.add_edge("3","4")
G.add_edge("3","5")
G.add_edge("4","5")
G.add_edge("2","6")
G.add_edge("4","6")
nx.draw(G, with_labels = True)
plt.savefig("networkx6.png")
# Ejecutar contra la QPU
sampler = EmbeddingComposite(DWaveSampler())
print(dnx.min_vertex_cover(G, sampler))