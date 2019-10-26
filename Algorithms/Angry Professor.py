t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = map(int, input().split())
    class_count = sum(
        1 if time <= 0 else 0
        for time in a
    )
    print(
        "YES" if class_count < k else "NO"
    )