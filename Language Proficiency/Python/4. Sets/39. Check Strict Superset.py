setA = set(input().split())
N = int(input())
verdict = True
for sets in range(N):
    setB = set(input().split())
    verdict = verdict & (setB < setA)

print(verdict)