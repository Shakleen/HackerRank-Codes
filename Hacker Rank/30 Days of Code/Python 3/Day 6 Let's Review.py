t = int(input())

for test in range(t):
    str = input()
    even, odd = str[::2], str[1::2]
    print('{0} {1}'.format(even, odd))
