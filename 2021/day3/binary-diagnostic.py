lines = []
with open('input.txt') as f:
  lines = f.readlines()

bitAvgArray = []

for i in range(len(lines)):
  binaryString = lines[i]
  bits = list(binaryString.strip())
  
  for j in range(len(bits)):
    bit = bits[j]

    if i == 0 and bit == '1':
      bitAvgArray.append(1)
    elif i == 0 and bit == '0':
      bitAvgArray.append(0)
    elif bit == '1':
      bitAvgArray[j] += 1

print(bitAvgArray)
print(len(lines))
print(len(lines) / 2)

gammaRate = []
epsilonRate = []

for k in range(len(bitAvgArray)):
  current1Total = bitAvgArray[k]
  if current1Total > (len(lines) / 2):
    gammaRate.append(1)
    epsilonRate.append(0)
  else:
    gammaRate.append(0)
    epsilonRate.append(1)

gammaBinaryString = ''.join(map(str, gammaRate))
epsilonBinaryString = ''.join(map(str, epsilonRate))

print('gamma', gammaBinaryString)
print('epsilon', epsilonBinaryString)

gammaDecimal = int(gammaBinaryString, 2)
epsilonDecimal = int(epsilonBinaryString, 2)
print('gamma decimal', gammaDecimal)
print('epsilon decimal', epsilonDecimal)

print('total energy', gammaDecimal * epsilonDecimal)
