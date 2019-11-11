import numpy as np

N = int(input())
A = np.array(
    [list(input().split()) for _ in range(N)],
    dtype = np.int32
)
B = np.array(
    [list(input().split()) for _ in range(N)],
    dtype = np.int32
)

print(np.dot(A, B))