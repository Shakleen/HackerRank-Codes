import numpy as np
np.set_printoptions(legacy='1.13')

N, M = input().split()
narr = np.array(
    [list(input().split()) for _ in range(int(N))],
    dtype = np.int32
)

print(np.mean(narr, axis = 1))
print(np.var(narr, axis = 0))
print(np.std(narr))