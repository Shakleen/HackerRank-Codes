n, k = map(int, input().split())
bill = list(map(int, input().split()))
calc = int(input())
real = sum(
    bill[i] 
    for i in range(len(bill)) 
    if i != k
) / 2

print(
    'Bon Appetit'
    if calc == real
    else int(calc - real)
)