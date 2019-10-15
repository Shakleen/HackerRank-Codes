import numpy as np

dim = tuple(map(int, input().split()))
print(np.zeros(dim, dtype = np.int32))
print(np.ones(dim, dtype = np.int32))