n = int(input())
s = list(map(int, input().split()))
d, m = map(int, input().split())

count = 0
for i in range(n-m+1):
    count += (sum(s[i : i+m]) == d)

print(count)