import numpy as np

narr = np.array(input().split(),np.float64)
k = int(input())
print(np.polyval(narr, k))