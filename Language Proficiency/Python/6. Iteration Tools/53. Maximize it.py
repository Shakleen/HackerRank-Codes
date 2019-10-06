import itertools as itt

K, M = map(int, input().split())
lists = []
maxVal = -1

def square_sum(arg):
    sum = 0
    for e in arg: sum += e ** 2
    return sum

for i in range(K):
    length, *L = map(int, input().split())
    lists.append(L)

for comb in itt.product(*lists):
    ssum = square_sum(comb)
    modded_ssum = ssum % M
    maxVal = max(maxVal, modded_ssum)

print(maxVal)