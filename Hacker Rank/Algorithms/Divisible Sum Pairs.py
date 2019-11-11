import itertools as itt

n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

for (i, j) in itt.product(range(n), range(n)):
    if (i < j): 
        count += ((arr[i] + arr[j]) % k == 0) 

print(count)