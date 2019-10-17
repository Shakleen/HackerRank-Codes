import numpy as np

N, M = map(int, input().split())
narr = np.array(
    [list(input().split()) for _ in range(N)],
    dtype = np.int32
)
print(
    np.product(
        np.sum(narr, axis = 0)
    )
)