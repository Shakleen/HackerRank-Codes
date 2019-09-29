def isPrime(no):
    if no < 2: return False

    for i in range(2, no):
        if i * i > no: break
        if no % i == 0: return False
    
    return True

T = int(input())
for i in range(T):
    n = int(input())
    print(
        "Prime" 
        if isPrime(n) 
        else "Not prime"
    )