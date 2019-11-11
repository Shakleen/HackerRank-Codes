import math

for test in range(int(input())):
    a, b = map(int, input().split())
    count = 0
    a_ps = math.ceil(math.sqrt(a))

    if a_ps * a_ps <= b:
        b_ps = math.floor(math.sqrt(b))
        count = b_ps - a_ps + 1

    print(count)