import numpy as np
N, M, P = map(int, input().split())
arr1 = [input().split() for i in range(N)]
arr2 = [input().split() for i in range(M)]
narr = np.concatenate((arr1, arr2))
print(narr.astype(np.int32))