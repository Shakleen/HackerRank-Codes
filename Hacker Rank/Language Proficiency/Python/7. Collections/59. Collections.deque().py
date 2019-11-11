from collections import deque

N = int(input())
d = deque()

for i in range(N):
    command = input().split()
    if len(command) > 1:
        exec('d.{c[0]}("{c[1]}")'.format(c=command))
    else:
        exec('d.{c[0]}()'.format(c=command))

print(' '.join(d))