n = int(input())
str = '{0} x {1} = {2}'
for i in range(1, 11):
    print(str.format(n, i, n*i))
