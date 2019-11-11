def produceAlphabetString(start, depth):
    L = []
    for i in range(1, depth+1):
        L.append(chr(97 + start - i))
    L = L[:-1] + L[::-1]
    return '-'.join(L)

def print_rangoli(size):
    paddingSize = 4 * size - 3
    for i in range(1, size+1):
        print(
            produceAlphabetString(size, i).center(paddingSize, '-')
        )

    for i in range(size-1, 0, -1):
        print(
            produceAlphabetString(size, i).center(paddingSize, '-')
        )

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)