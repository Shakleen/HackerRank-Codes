i, j, k = map(int, input().split())
count = 0

for day in range(i, j+1):
    rev = int(str(day)[::-1])
    count += (abs(day-rev) % k == 0)

print(count)