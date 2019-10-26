n = int(input())
total_liked = 0
people = 5

for i in range(n):
    liked = people // 2
    total_liked += liked
    people = liked * 3

print(total_liked)