import itertools as itt

n, m = map(int, input().split())
knowledge = [
    input()
    for _ in range(n)
]
pair_knowledge = {}
all_comb = itt.product(range(n), range(n))

for (i, j) in all_comb:
    if i == j: continue
    a = eval('0b' + knowledge[i])
    b = eval('0b' + knowledge[j])
    tot = bin(a | b).count('1')
    pair_knowledge[tot] = pair_knowledge.get(tot, 0) + 1

max_knowledge = max(pair_knowledge)
print(max_knowledge)
print(pair_knowledge[max_knowledge])