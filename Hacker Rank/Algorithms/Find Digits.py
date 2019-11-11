tests = int(input())

for test in range(tests):
    number = int(input())
    count = 0
    
    for digit in str(number):
        if digit == '0': continue
        count += ((number % int(digit)) == 0)
    
    print(count)