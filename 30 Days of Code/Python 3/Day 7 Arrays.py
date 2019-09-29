n = int(input())
arr = list(map(int, input().rstrip().split()))
revArr = arr[::-1]
for item in revArr: print(item, end=' ')
