from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for tup in product(A, B):
    print(tup, end=' ')