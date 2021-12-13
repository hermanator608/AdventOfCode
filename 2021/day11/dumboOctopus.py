import os.path
import math
from typing import Counter

dirname = os.path.abspath(os.path.dirname(__file__))
inputPath = os.path.join(dirname, "./input.txt")

lines = []
with open(inputPath) as f:
  lines = f.readlines()

totalFlashes = 0


def printMap(map, step):
  print(f'-------- Map (Step {step}) --------')
  for i in map:
    print(i)
  print(f'------------------------------')


def explode(map, i, j):
  global totalFlashes

  # Out of bounds
  if (i < 0 or i >= len(map) or j < 0 or j >= len(map[i])):
    return

  # Already exploded this step
  if (map[i][j] == 0):
    return

  map[i][j] = map[i][j] + 1

  if (map[i][j] > 9):
    totalFlashes += 1
    map[i][j] = 0
    explode(map, i - 1, j - 1)
    explode(map, i - 1, j)
    explode(map, i - 1, j + 1)
    explode(map, i, j - 1)
    explode(map, i, j + 1)
    explode(map, i + 1, j - 1)
    explode(map, i + 1, j)
    explode(map, i + 1, j + 1)

def startExploding(map):
  for i in range(len(map)):
    for j in range(len(map[i])):
      if (map[i][j] > 9):
        explode(map, i, j)

def powerUp(map):
  for i in range(len(map)):
    for j in range(len(map[i])):
      map[i][j] = map[i][j] + 1

octopusMap = []
for i in range(len(lines)):
  line = [int(i) for i in list(lines[i].strip())]
  octopusMap.append(line)

printMap(octopusMap, 0)

# Part 1
# for i in range(100):
#   powerUp(octopusMap)
#   startExploding(octopusMap)

#   printMap(octopusMap, i)



# Part 2
def didAllExplode(map):
  areAllZero = True
  for i in range(len(map)):
    if (areAllZero == False):
      break

    for j in range(len(map[i])):
      if (map[i][j] != 0):
        areAllZero = False
        break

  return areAllZero

didAllFlash = False
stepCounter = 1
while (not didAllFlash):

  powerUp(octopusMap)
  startExploding(octopusMap)
  printMap(octopusMap, stepCounter)

  if (didAllExplode(octopusMap)):
    didAllFlash = True
    print('Synchronous Flash at Step: ', stepCounter)

  stepCounter += 1

print('Total Flashes:', totalFlashes)
