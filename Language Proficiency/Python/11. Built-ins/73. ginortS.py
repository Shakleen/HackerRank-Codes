s = list(input())

def func(char):
    if 'a' <= char <= 'z':
        return ord(char) - 9000
    elif 'A' <= char <= 'Z':
        return ord(char) - 900
    elif int(char) % 2 != 0:
        return ord(char) - 90
    else:
        return ord(char)

s.sort(key = func)
print(''.join(s))