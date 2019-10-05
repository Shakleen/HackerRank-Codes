from itertools import permutations
s, k = input().split()
for p in permutations(sorted(s), int(k)): print(''.join(p))