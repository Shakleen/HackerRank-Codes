heights = {}
for (k, v) in zip(
        range(ord('a'), ord('z') + 1),
        map(int, input().split())
    ):
    heights[k] = v

s = input()
max_height = max(
    s,
    key = lambda x: heights[ord(x)]
)
print(len(s) * heights[ord(max_height)])