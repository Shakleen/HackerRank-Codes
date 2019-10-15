import numpy

def arrays(arr):
    narr = numpy.array(arr)
    return narr[::-1].astype(numpy.float64)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)