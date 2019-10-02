k = int(input())
rooms = list(input().split())
unique = set()
notUnique = set()

for room in rooms:
    if room in notUnique: 
        continue
    elif room in unique:
        unique.remove(room)
        notUnique.add(room)
    elif room not in unique:
        unique.add(room)

print(''.join(unique))