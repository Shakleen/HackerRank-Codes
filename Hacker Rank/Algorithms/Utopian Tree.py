heights = [1]

for i in range(1, 61):
    heights.append(
        heights[i-1] + 
        (1 if i % 2 == 0 else heights[i-1])
    )

t = int(input())
for i in range(t):
    n = int(input())
    print(heights[n])