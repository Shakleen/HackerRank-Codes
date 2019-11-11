import numpy as np

N, M = map(int, input().split())
arr = [list(input().split()) for i in range(N)]
narr = np.array(arr, dtype = np.int32)
print(narr.T)
print(narr.flatten())