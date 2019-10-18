import numpy as np
np.set_printoptions(legacy='1.13')

N = int(input())
narr = np.array(
    [list(input().split()) for _ in range(N)],
    dtype = np.float64
)
print(np.linalg.det(narr))