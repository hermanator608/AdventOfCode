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

  if graph.get(info[1]) is not None:
    graph[info[1]].append(info[0])
  else:
    graph[info[1]] = [info[0]]

print(graph)

def findPaths(graph, start, end, canGoInSmallCaveAgain, path = []):
  path = path + [start]

  if start == end:
    return [path]

  if not graph.get(start):
    return []

  paths = []
  for p in graph[start]:
    if p.islower() and p in path:
      if canGoInSmallCaveAgain and p != 'start' and p != 'end':
        newPaths = findPaths(graph, p, end, False, path)
        paths = paths + newPaths
    else:
      newPaths = findPaths(graph, p, end, canGoInSmallCaveAgain, path)
      paths = paths + newPaths
  return paths

paths = findPaths(graph, 'start', 'end', True)
# print(paths)
print(len(paths))
# Part 1: 4573
