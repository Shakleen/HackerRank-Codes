x1, v1, x2, v2 = map(
    int,
    input().split()
)

possible = False

if x1 < x2 and v1 < v2: possible = False
elif x1 > x2 and v1 > v2: possible = False
elif v1 == v2: possible = (x1 == x2)
else:
    k = (x1 - x2) / (v2 - v1)
    possible = (int(k) == k)

print("YES" if possible else "NO")