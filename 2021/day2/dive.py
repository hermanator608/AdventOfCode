from enum import Enum

lines = []
with open('input.txt') as f:
  lines = f.readlines()

class Action(Enum):
  FORWARD = 'forward'
  DOWN = 'down'
  UP = 'up'

depth = 0
horizontal = 0
aim = 0

for i in range(len(lines)):
  data = lines[i].split()
  actionName = data[0]
  actionAmount = int(data[1])

  if actionName == Action.FORWARD.value:
    horizontal += actionAmount
    depth += (actionAmount * aim)
  elif actionName == Action.DOWN.value:
    aim += actionAmount
  elif actionName == Action.UP.value:
    aim -= actionAmount


print('depth', depth)
print('horizontal', horizontal)
print('Product: ', depth * horizontal)
