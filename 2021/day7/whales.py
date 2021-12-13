import numpy as np
import math
import os.path

dirname = os.path.abspath(os.path.dirname(__file__))
inputPath = os.path.join(dirname, "./input.txt")

lines = []
with open(inputPath) as f:
  lines = f.readlines()

data = list(map(int, lines[0].strip().split(',')))

print(data)


# Part 1
# dataNp = np.array(data)
# med = np.median(dataNp)
# medLower, medHigher = math.floor(med), math.ceil(med)
# distLower = np.sum(np.absolute(dataNp - medLower))
# distHigher = np.sum(np.absolute(dataNp - medHigher))
# print(distHigher, distLower)

# part 2
dataNp = np.array(data)
mean = np.mean(dataNp)
meanLower, meanHigher = math.floor(mean), math.ceil(mean)
distsLower = np.absolute(dataNp - meanLower)
distsHigher = np.absolute(dataNp - meanHigher)
distLower = np.sum((distsLower ** 2 + distsLower)/2)
distHigher = np.sum((distsHigher ** 2 + distsHigher)/2)


print(min(distHigher, distLower))
