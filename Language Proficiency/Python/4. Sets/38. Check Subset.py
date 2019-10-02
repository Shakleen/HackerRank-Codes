T = int(input())

for test in range(T):
    n = int(input())
    setA = set(input().split())
    m = int(input())
    setB = set(input().split())
    print(setA <= setB)