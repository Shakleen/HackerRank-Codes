import math

low = int(input())
high = int(input())
results = []

for n in range(low, high+1):
    sqN = n * n
    digitsN = 1 + int(math.log10(n))
    splitter = 10 ** digitsN
    right = sqN % splitter
    left = (sqN - right) // splitter
    sum = left + right

    if sum == n:
        results.append(n)

print(
    ' '.join(map(str, results))
    if results else
    'INVALID RANGE'
)