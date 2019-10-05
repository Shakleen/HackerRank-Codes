from itertools import groupby
s = input()
for key, val in groupby(s):
    print('({0}, {1})'.format(len(list(val)), key), end=' ')