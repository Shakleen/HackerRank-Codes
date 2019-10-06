import itertools

N = int(input())
L = list(input().split())
K = int(input())
count = total = 0

all_pos_combs = itertools.combinations(L, K)
for comb in all_pos_combs: 
    if 'a' in comb: count += 1
    total += 1
    
print(count / total)