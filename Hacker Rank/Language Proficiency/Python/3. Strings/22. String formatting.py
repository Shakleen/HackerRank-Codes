def print_formatted(number):
    strForm = '{0:>{4}} {1:>{4}} {2:>{4}} {3:>{4}}'
    width = len(bin(number)[2:])
    for no in range(1, number+1):
        binary = bin(no)[2:]
        octal = oct(no)[2:]
        hexaDecimal = hex(no)[2:].upper()
        print(
            strForm.format(
                no, 
                octal, 
                hexaDecimal, 
                binary,
                width
            )
        )

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)