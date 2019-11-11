n = int(input())
sightings = list(map(int, input().split()))
occurrances = {}

for id in sightings:
    occurrances[id] = occurrances.get(id, 0) + 1

max_idx = -1
mx = -1
for o in sorted(occurrances):
    if occurrances[o] > mx:
        mx = occurrances[o]
        max_idx = o

print(max_idx)