n = int(input())
Set = set(map(int, input().split()))
noOfCommands = int(input())

for i in range(noOfCommands):
    command = list(input().split())

    try:
        if command[0] == 'pop': 
            Set.pop()
        elif command[0] == 'remove':
            Set.remove(int(command[1]))
        elif command[0] == 'discard':
            Set.discard(int(command[1]))
    except KeyError:
        continue

print(sum(Set))
