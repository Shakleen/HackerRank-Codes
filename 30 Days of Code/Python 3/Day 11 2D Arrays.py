arr2d = []

for i in range(6):
    arr = list(map(int, input().rstrip().rsplit()))
    arr2d.append(arr)

maxSum = -9999999
for i in range(4):
    for j in range(4):
        topHalf = arr2d[i][j] + arr2d[i][j+1] + arr2d[i][j+2]
        bottomHalf = arr2d[i+2][j] + arr2d[i+2][j+1] + arr2d[i+2][j+2]
        sum = topHalf + arr2d[i+1][j+1] + bottomHalf
        maxSum = max(sum, maxSum)

print(maxSum)