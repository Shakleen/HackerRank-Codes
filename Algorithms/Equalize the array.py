n = int(input())
arr = list(map(int, input().split()))
freq = {}

for val in arr: freq[val] = freq.get(val, 0) + 1

max_idx = max_val = -1
for key in freq:
    if freq[key] > max_val:
        max_val, max_idx = freq[key], key


print(len(arr) - max_val)
