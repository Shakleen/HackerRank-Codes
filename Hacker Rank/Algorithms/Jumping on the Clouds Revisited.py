n, k = map(int, input().split())
c = list(map(int, input().split()))
e, idx = 100, 0

while True:
    idx = (idx + k) % n
    e -= (1 + 2 * c[idx])
    if idx == 0: break

print(e)