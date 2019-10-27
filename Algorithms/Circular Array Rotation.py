n, k, q = map(int, input().split())
a = list(map(int, input().split()))
k %= n
for _ in range(q):
    m = int(input())
    print(a[(n+ m - k) % n])