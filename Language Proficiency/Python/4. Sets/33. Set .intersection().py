n = int(input())
englishSubs = set(map(int, input().split()))
m = int(input())
frenchSubs = set(map(int, input().split()))
both = englishSubs & frenchSubs
print(len(both))