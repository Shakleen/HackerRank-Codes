import numpy as np

A = np.array(
    list(input().split()),
    dtype = np.int32
)
B = np.array(
    list(input().split()),
    dtype = np.int32
)

print(np.inner(A, B))
print(np.outer(A, B))