arr = list(map(int, input().split()))
arr.sort()

print(
    '{min} {max}'.format(
        min = sum(arr[:-1]),
        max = sum(arr[1:])
    )
)