for _ in range(int(input())):
    b, w = map(int, input().split())
    bc, wc, z = map(int, input().split())
    b_cost = min(bc, wc + z)
    w_cost = min(wc, bc + z)
    total = b * b_cost + w * w_cost
    print(total)