N = int(input())
arr = [input().split() for _ in range(N)]
trace1 = trace2 = 0

for i in range(N):
    trace1 += int(arr[i][i])
    trace2 += int(arr[i][N-i-1])

print(abs(trace1 - trace2))