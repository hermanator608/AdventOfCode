import os.path
import math
from typing import Counter

dirname = os.path.abspath(os.path.dirname(__file__))
dotsInputPath = os.path.join(dirname, "./dots.txt")
instructionsInputPath = os.path.join(dirname, "./instructions.txt")
# dotsInputPath = os.path.join(dirname, "./easyDots.txt")
# instructionsInputPath = os.path.join(dirname, "./easyInstructions.txt")

dotsLines = []
with open(dotsInputPath) as f:
  dotsLines = f.readlines()

instructionsLines = []
with open(instructionsInputPath) as f:
  instructionsLines = f.readlines()

intructions = []
for i in range(len(instructionsLines)):
  instruct = instructionsLines[i].strip().split("fold along ", 1)[1]
  instructInfo = instruct.split('=')

  direction = instructInfo[0]
  location = int(instructInfo[1])

  intructions.append((direction, location))

def printMap(map, foldNum):
  print(f'-------- Map (Fold {foldNum}) --------')
  for i in map:
    print(i)
  print(f'------------------------------')

def createMap(dotsLines):
  height = 0
  width = 0
  pos = []
  for i in range(len(dotsLines)):
    val = dotsLines[i].strip().split(',')

    # Flipped due to how we index arrays by y first in python
    y = int(val[0])
    x = int(val[1])
    pos.append((x, y))
    width = y if y > width else width
    height = x if x > height else height

  paper = [[0 for i in range(width + 1)] for j in range(height + 1)]

  print(len(paper), len(paper[0]))
  for val in pos:
    print(val[0],val[1])
    paper[val[0]][val[1]] = 1

  printMap(paper, 0)
  return paper

def fold(map, instruction):
  direction, location = instruction
  newMap = []

  if (direction == 'x'):
    print('x fold', location)
    leftCut = [map[i][:location] for i in range(len(map))]
    rightCut = [map[i][(location+1):] for i in range(len(map))]

    # Only works if we are folding in half
    newMap = [[0 for i in range(len(leftCut[0]))] for j in range(len(leftCut))]
    for i in range(len(leftCut)):
      for j in range(len(leftCut[i])):
        newMap[i][j] = 1 if leftCut[i][j] == 1 or rightCut[i][-(j + 1)] == 1 else 0

  elif (direction == 'y'):
    print('y fold', location)
    topCut = [map[i] for i in range(0,location)]
    bottomCut = [map[i] for i in range(location + 1, len(map))]

    # Only works if we are folding in half
    newMap = [[0 for i in range(len(topCut[0]))] for j in range(len(topCut))]
    for i in range(len(topCut)):
      for j in range(len(topCut[i])):
        newMap[i][j] = 1 if topCut[i][j] == 1 or bottomCut[-(i + 1)][j] == 1 else 0

  printMap(newMap, 1)
  return newMap

def countDots(map):
  count = 0
  for i in range(len(map)):
    for j in range(len(map[i])):
      count += map[i][j]
  return count

# Part 1
# map = createMap(dotsLines)
# foldedMap = fold(map, intructions[0])
# dots = countDots(foldedMap)
# print(dots)

# Part 2
map = createMap(dotsLines)
for i in intructions:
  map = fold(map, i)

dots = countDots(map)
print(dots)
# [1,       1,    1, 1, 1, 1,          1, 1,    1,       1,          1, 1,    1, 1, 1,          1, 1,             1, 1]
# [1,       1,    1,                      1,    1,       1,             1,    1,       1,    1,       1,             1]
# [1, 1, 1, 1,    1, 1, 1,                1,    1, 1, 1, 1,             1,    1,       1,    1,                      1]
# [1,       1,    1,                      1,    1,       1,             1,    1, 1, 1,       1,                      1]
# [1,       1,    1,             1,       1,    1,       1,    1,       1,    1,    1,       1,       1,    1,       1]
# [1,       1,    1, 1, 1, 1,       1, 1,       1,       1,       1, 1,       1,       1,       1, 1,          1, 1,  ]
