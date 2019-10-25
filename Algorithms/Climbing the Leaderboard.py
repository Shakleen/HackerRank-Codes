def binary_search(key):
    low = 0
    high = len(scores) - 1
    result = 0

    while low <= high:
        mid = (low + high) // 2

        if scores[mid] >= key:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return result

n = int(input())
scores = sorted(set(map(
    int, input().split()
)), reverse = True)

m = int(input())
alice = map(int, input().split())

for a in alice:
    rank = binary_search(a)

    if a < scores[rank]:
        rank += 1

    print(rank + 1)