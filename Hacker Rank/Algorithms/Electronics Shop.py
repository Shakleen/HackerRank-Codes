import itertools as itt

b, n, m = map(int, input().split())
keyboard_prices = list(map(int, input().split()))
drive_prices = list(map(int, input().split()))
spend = -1

for (k_price, d_price) in itt.product(keyboard_prices, drive_prices):
    total = k_price + d_price

    if total <= b:
        spend = max(total, spend)

    if spend == b: break

print(spend)