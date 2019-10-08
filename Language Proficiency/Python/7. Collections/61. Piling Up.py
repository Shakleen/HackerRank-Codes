tests = int(input())

def findMax(l): return (l[0], 0) if l[0] > l[-1] else (l[-1], len(l)-1)

for case in range(tests):
    cubes = int(input())
    sideLengths = list(map(int, input().split()))
    prev = -1

    while sideLengths:
        maxVal, maxIdx = findMax(sideLengths)
        
        if prev == -1: 
            prev = maxVal
        elif prev < maxVal:
            print('No')
            break
        else:
            sideLengths.pop(maxIdx)
            prev = maxVal
    else:
        print('Yes')