import textwrap

def merge_the_tools(string, k):
    L = textwrap.wrap(string, k)
    for e in L:
        S = set()
        for char in e:
            if char not in S:
                S.add(char)
                print(char, end='')
        print('')

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)