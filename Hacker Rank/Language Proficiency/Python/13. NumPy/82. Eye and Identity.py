import numpy as np

N, M = map(int, input().split())
np.set_printoptions(legacy='1.13')
print(np.eye(N, M, k = 0, dtype = np.float64))