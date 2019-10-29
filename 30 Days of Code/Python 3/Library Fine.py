d1, m1, y1 = map(int, input().split())
d2, m2, y2 = map(int, input().split())
fine = 0

if y1 > y2:
    fine = 10000
elif y1 == y2:
    if m1 > m2:
        fine = (m1 - m2) * 500
    elif m1 == m2:
        if d1 > d2:
            fine = (d1 - d2) * 15

print(fine)