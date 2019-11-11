import numpy as np

N, M = map(int, input().split())

narr = np.array(
    [list(input().split()) for _ in range(N)],
    dtype = np.int32
)

print(
    np.max(
        np.min(narr, axis = 1)
    )
)