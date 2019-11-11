def split_and_join(line):
    L = line.split(' ')
    return '-'.join(L)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)