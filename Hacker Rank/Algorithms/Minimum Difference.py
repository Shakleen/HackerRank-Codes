size = int(input())
noList = list(
    map(int, input().split())
)
minDiff = size + 1
prevIndex = {}

for i in range(size):
    val = noList[i]

    if val in prevIndex:
        minDiff = min(
            minDiff,
            i - prevIndex[val]
        )
    
    prevIndex[val] = i

print(
    minDiff
    if minDiff <= size
    else -1
)