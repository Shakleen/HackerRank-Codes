def takeIntInput(): 
    return map(int, input().split())

def findCorrectValue(i):
    try:
        return noList.index(noList[i] + diff, i+1, numbers)
    except ValueError:
        return -1

numbers, diff = takeIntInput()
noList = list(takeIntInput())
count = 0

for i in range(numbers - 2):
    j = findCorrectValue(i)
    k = -1 if j == -1 else findCorrectValue(j)
    count += (j != -1 and k != -1)

print(count)