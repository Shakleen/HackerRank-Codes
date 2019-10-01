N = int(input())
distinct = set()

for i in range(N):
    countryName = input()
    distinct.add(countryName)

print(len(distinct))