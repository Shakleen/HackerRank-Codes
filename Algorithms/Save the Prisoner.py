t = int(input())

for _ in range(t):
    n, m, s = map(int, input().split())
    m %= n
    chair_no = (s + m - 1) % n
    print(
        chair_no 
        if chair_no != 0
        else n
    )