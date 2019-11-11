n, m = map(int, input().rstrip().rsplit())
array = list(map(int, input().rstrip().rsplit()))
setA = set(map(int, input().rstrip().rsplit()))
setB = set(map(int, input().rstrip().rsplit()))
happiness = 0
for e in array:
    if e in setA: happiness += 1
    if e in setB: happiness -= 1
print(happiness)