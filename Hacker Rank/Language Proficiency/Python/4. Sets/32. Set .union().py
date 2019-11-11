n = int(input())
englishSubs = set(map(int, input().split()))
m = int(input())
frenchSubs = set(map(int, input().split()))
atLeastOne = englishSubs | frenchSubs
print(len(atLeastOne))