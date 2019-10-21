from math import gcd
from functools import reduce
lcm = lambda x, y: (x * y) // gcd(x, y)

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

gcd_b = reduce(gcd, b)
lcm_a = reduce(lcm, a)
count = sum(
    gcd_b % no == 0 
    for no in range(lcm_a, gcd_b+1, lcm_a)
)

print(count)