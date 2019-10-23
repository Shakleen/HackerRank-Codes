n = int(input())
trackings = input()
count = sum = 0

for t in trackings:
    a = 1 if t == 'U' else -1
    if sum < 0:
        count += (sum + a == 0)
    sum += a
    
print(count)