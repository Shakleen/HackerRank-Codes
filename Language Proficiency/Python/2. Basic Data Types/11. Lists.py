if __name__ == '__main__':
    L = []
    N = int(input())

    for _ in range(N):
        command = input().rstrip().rsplit()

        if command[0] == 'insert':
            i = int(command[1])
            e = int(command[2])
            L.insert(i, e)
        elif command[0] == 'print':
            print(L)
        elif command[0] == 'remove':
            e = int(command[1])
            L.remove(e)
        elif command[0] == 'append':
            e = int(command[1])
            L.append(e)
        elif command[0] == 'pop':
            L.pop()
        elif command[0] == 'reverse':
            L.reverse()
        elif command[0] == 'sort':
            L.sort()
