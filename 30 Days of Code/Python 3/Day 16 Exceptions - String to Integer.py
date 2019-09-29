s = input().strip()

try:
    val = int(s)
    print(val)
except ValueError:
    print('Bad String')
    