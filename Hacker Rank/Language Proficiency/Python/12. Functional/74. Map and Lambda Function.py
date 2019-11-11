cube = lambda x: x ** 3

def fibonacci(n):
    fibo = []
    for i in range(n): fibo.append(i if i <= 1 else fibo[i-1] + fibo[i-2])
    return fibo


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))