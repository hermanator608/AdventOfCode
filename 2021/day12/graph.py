import networkx as nx
import matplotlib.pyplot as plt
import os.path

dirname = os.path.abspath(os.path.dirname(__file__))
inputPath = os.path.join(dirname, "./input.txt")

lines = []
with open(inputPath) as f:
  lines = f.readlines()

graph = {}
for i in range(len(lines)):
  info = lines[i].strip().split('-')

  if graph.get(info[0]) is not None:
    graph[info[0]].append(info[1])
  else:
    graph[info[0]] = [info[1]]

nxGraph = nx.Graph()

for node, otherNodes in graph.items():
    if node not in nxGraph:
        nxGraph.add_node(node)

    for otherNode in otherNodes:
        if otherNode not in nxGraph:
            nxGraph.add_node(otherNode)

        nxGraph.add_edge(node, otherNode)

nx.draw(
    nxGraph,pos = nx.layout.spring_layout(
        nxGraph,
        pos={'start':(0,1), 'end':(0,-1)},
        fixed=['start','end']),
        with_labels = True,
        font_weight='bold',

    )
plt.show()
