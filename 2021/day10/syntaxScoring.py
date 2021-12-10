import os.path
import math

dirname = os.path.abspath(os.path.dirname(__file__))
inputPath = os.path.join(dirname, "./input.txt")

lines = []
with open(inputPath) as f:
  lines = f.readlines()

# Could probably do something to not have all these different maps
openingType = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>'
}

closingType = {
  ')': '(',
  ']': '[',
  '}': '{',
  '>': '<'
}

corruptedScoreMap = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137,
}

incompleteScoreMap = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4,
}

openingStack = []

corruptedScore = 0
autoCompleteScores = []

for i in range(len(lines)):
  line = lines[i].strip()
  
  # Clear stacks for each line
  openingStack = []

  notCorrupted = True
  for j in range(len(line)):
    char = line[j]

    if openingType.get(char):
      openingStack.append(char)
    elif closingType.get(char):
      lastOpeningChar = openingStack.pop(-1)

      if lastOpeningChar != closingType[char]:
        print(line, '- Expected ', openingType.get(lastOpeningChar), 'but found ', char, 'instead.')
        corruptedScore += corruptedScoreMap[char]
        notCorrupted = False
        break
  
  if notCorrupted and len(openingStack) > 0:
    autoCompleteArray = []
    autoCompleteTempScore = 0
    while len(openingStack) > 0:
      openChar = openingStack.pop(-1)
      autoCompleteArray.append(openingType.get(openChar))

    for k in range(len(autoCompleteArray)):
      closingChar = autoCompleteArray[k]

      autoCompleteTempScore *= 5
      autoCompleteTempScore += incompleteScoreMap[closingChar]

    autoCompleteScores.append(autoCompleteTempScore)
    print(line, '- Complete by adding ', ''.join(map(str, autoCompleteArray)), ' - CompleteScore: ', autoCompleteTempScore)


autoCompleteScores.sort()
print(autoCompleteScores)
middleIndex = math.ceil(len(autoCompleteScores) / 2)

print('Syntax score', corruptedScore)
print('Autocomplete Middle Score', autoCompleteScores[middleIndex - 1])
