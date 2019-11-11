name = input()
occurances = [0 for i in range(26)]
for char in name: occurances[ord(char)-97] += 1

for i in range(3):
    maxVal = max(occurances)
    minIdxList = occurances.index(maxVal)
    minIdx = min(minIdxList) if isinstance(minIdxList, list) else minIdxList
    occurances[minIdx] = -1
    print('{char} {freq}'.format(char=chr(minIdx+97), freq=maxVal))
