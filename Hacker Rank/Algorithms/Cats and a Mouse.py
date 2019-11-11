q = int(input())

for i in range(q):
    x, y, z = map(int, input().split())

    cat_a = abs(x - z)
    cat_b = abs(y - z)

    if cat_a == cat_b:
        print('Mouse C')
    elif cat_a < cat_b:
        print('Cat A')
    else:
        print('Cat B')
