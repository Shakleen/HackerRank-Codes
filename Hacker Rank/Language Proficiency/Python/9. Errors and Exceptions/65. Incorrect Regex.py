import re

T = int(input())

for t in range(T):
    exp = input()

    try:
        re.search(exp, 'kdaklsj')
        print('True')
    except Exception:
        print('False')