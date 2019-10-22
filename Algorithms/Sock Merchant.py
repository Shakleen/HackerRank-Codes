n = int(input())
socks = list(map(int, input().split()))
pairs = {}
for sock in socks: pairs[sock] = pairs.get(sock, 0) + 0.5
total = sum(
    int(pairs[sock])
    for sock in pairs
)
print(total)