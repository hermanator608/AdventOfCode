lines = []
with open('input.txt') as f:
  lines = f.readlines()

count = 0
previousSum = None
for i in range(len(lines)):
  if i == 0:
    previousSum = int(lines[0]) + int(lines[1]) + int(lines[2])
    continue
  elif i == len(lines) - 1:
    continue

  currentMeasurementSum = int(lines[i-1]) + int(lines[i]) + int(lines[i+1])

  if previousSum != None and previousSum < currentMeasurementSum:
    count += 1
  
  previousSum = currentMeasurementSum


print(count)
