n = int(input())
str = bin(n)[2:]
max1s = 0
ones = 0

for no in str:
    if no == '1': 
        ones += 1
    else: 
        max1s = max(ones, max1s)
        ones = 0

max1s = max(ones, max1s)
print(max1s)
