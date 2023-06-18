import networkx as nx
from minorminer import busclique
import matplotlib.pyplot as plt
import dwave_networkx as dnx

triangle_graph = nx.complete_graph(3)
triangle_edge = triangle_graph.edges()
node_colors = [[0.8,.34,.167], 'yellow', 'orange']
nx.draw(triangle_graph,with_labels = True,node_color = node_colors)
plt.show()

print(triangle)