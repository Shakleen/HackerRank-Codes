n = int(input())
a = list(map(int, input().split()))
freq = {}

for i in a:
    freq[i] = freq.get(i, 0) + 1

no_sorted = sorted(freq)
max_len = freq[no_sorted[0]]

for i in range(1, len(no_sorted)):
    comp = [max_len, freq[no_sorted[i]]]
    diff = abs(no_sorted[i-1] - no_sorted[i])

    if diff <= 1:
        comp.append(
            freq[no_sorted[i-1]] + freq[no_sorted[i]]
        )
    
    max_len = max(comp)

print(max_len)