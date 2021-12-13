import os.path

dirname = os.path.abspath(os.path.dirname(__file__))
inputPath = os.path.join(dirname, "./input.txt")

lines = []
with open(inputPath) as f:
  lines = f.readlines()

map = []
for i in range(len(lines)):
  line = [int(i) for i in list(lines[i].strip())]
  map.append(line)

count = 0
for i in range(len(map)):
  for j in range(len(map[i])):
    if i != 0 and map[i-1][j] <= map[i][j]:
      continue
    if j != 0 and map[i][j-1] <= map[i][j]:
      continue
    if i != 99 and map[i+1][j] <= map[i][j]:
      continue
    if j != 99 and map[i][j+1] <= map[i][j]:
      continue
    count += 1 + map[i][j]

print(count)
