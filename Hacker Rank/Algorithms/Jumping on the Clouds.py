n = int(input())
c = list(map(int, input().split()))
count = 0
idx = 0

while idx < n-1:
    count += 1

    if idx+2 < n and c[idx+2] != 1: 
        idx += 2
    else: 
        idx += 1
        

print(count)
