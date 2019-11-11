def swap_case(s):
    L = list(s)
    for pos in range(len(L)):
        if L[pos].isalpha:
            L[pos] = L[pos].lower() if L[pos].isupper() else L[pos].upper()
    return ''.join(L)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)