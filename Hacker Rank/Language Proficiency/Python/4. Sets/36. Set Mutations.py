n = int(input())
setA = set(map(int, input().split()))
N = int(input())

for i in range(N):
    command = list(input().split())
    setB = set(map(int, input().split()))
    exec('setA.{}(setB)'.format(command[0]))

print(sum(setA))