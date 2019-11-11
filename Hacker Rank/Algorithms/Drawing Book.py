n = int(input())
p = int(input())

turns = -1
if p == 1 or p == n:
    turns = 0
else:
    turns = min(p // 2, (n - p + (n % 2 == 0)) // 2)

print(turns)