import collections as col
X = int(input())
sizeAmount = col.Counter(map(int, input().split()))
N = int(input())
totalEarning = 0

for i in range(N):
    shoeSize, price = map(int, input().split())
    if shoeSize in sizeAmount:
        if sizeAmount[shoeSize] > 0:
            totalEarning += price
            sizeAmount[shoeSize] -= 1

print(totalEarning)
