s = input()
t = input()
k = int(input())
msg = "No"

if k >= len(s) + len(t):
    msg = "Yes"
else:
    same_idx = 0

    for i in range(min(len(s), len(t))):
        if s[i] != t[i]: break
        same_idx = i + 1
    
    op_needed = (len(s) - same_idx) + (len(t) - same_idx)

    if op_needed <= k and (k - op_needed) % 2 == 0:
        msg = "Yes"

print(msg)