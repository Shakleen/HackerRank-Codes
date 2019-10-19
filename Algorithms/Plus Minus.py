n = int(input())
arr = list(map(int, input().split()))
pos = neg = zeros = 0
for val in arr:
    pos += val > 0
    neg += val < 0
    zeros += val == 0

s = '{:.6f}'
print(s.format(pos/n))
print(s.format(neg/n))
print(s.format(zeros/n))