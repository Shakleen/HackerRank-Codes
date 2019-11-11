n, m = map(int, input().split())
wordGroupA = {}

for i in range(n): 
    char = input()
    if char in wordGroupA:
        wordGroupA[char].append(str(i+1))
    else:
        wordGroupA[char] = [str(i+1)]

for i in range(m):
    indices = wordGroupA.get(input(), ['-1'])
    print(' '.join(indices))