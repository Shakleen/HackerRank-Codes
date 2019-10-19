n = int(input())
s = '{space}{symbol}'

for i in range(n):
    print(('#' * (i + 1)).rjust(n, ' '))