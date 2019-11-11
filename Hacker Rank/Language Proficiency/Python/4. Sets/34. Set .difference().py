n = int(input())
englishSubs = set(map(int, input().split()))
m = int(input())
frenchSubs = set(map(int, input().split()))
onlyEnglish = englishSubs - frenchSubs
print(len(onlyEnglish))