n = int(input())
a = list(map(int, input().split()))
mapped = {}
for e in a: mapped[a[a[e-1]-1]] = e
for k in sorted(mapped): print(mapped[k])