import numpy as np

N, M = map(int, input().split())

a = np.array(
    [input().split() for _ in range(N)], 
    dtype = np.int32
).reshape(N, M)

b = np.array(
    [input().split() for _ in range(N)], 
    dtype = np.int32
).reshape(N, M)

print(np.add(a, b).astype(np.int32))
print(np.subtract(a, b).astype(np.int32))
print(np.multiply(a, b).astype(np.int32))
print(np.divide(a, b).astype(np.int32))
print(np.mod(a, b).astype(np.int32))
print(np.power(a, b).astype(np.int32))
