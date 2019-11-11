n, k = map(int, input().split())
max_height = max(
    map(int, input().split())
)
print(
    0
    if max_height <= k
    else max_height - k
)