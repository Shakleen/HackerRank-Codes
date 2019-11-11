n = int(input())
scores = list(map(int, input().split()))

mn = 10 ** 8 + 1
mx = -1
count = [-1, -1]

for score in scores:
    count[0] += score > mx
    count[1] += score < mn
    mx = max(score, mx)
    mn = min(score, mn)

print('{c[0]} {c[1]}'.format(c=count))