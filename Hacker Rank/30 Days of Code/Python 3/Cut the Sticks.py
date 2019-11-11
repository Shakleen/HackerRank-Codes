n = int(input())
a = list(map(int, input().split()))

while a:
    print(len(a))
    min_val = min(a)
    a = list(
        filter(
            lambda x: x,
            map(
                lambda x: x - min_val,
                a
            )
        )
    )