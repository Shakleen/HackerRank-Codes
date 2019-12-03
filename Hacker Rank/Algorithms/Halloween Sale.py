import math

p, d, m, s = map(int, input().split())
n = math.ceil((p - m) / d)
sum = lambda x: int((x / 2) * (2 * p + (x - 1) * d))
count = n
spent = sum(count)

if spent < s:
    count += (s - spent) // m
elif spent > s:
    while sum(count) > s:
        count -= 1

print(count)