from collections import OrderedDict
listOfItems = OrderedDict()
N = int(input())

for i in range(N):
    *name, price = input().split()
    name = ' '.join(name)
    listOfItems[name] = int(price) + listOfItems.get(name, 0)

for name in listOfItems:
    print('{name} {price}'.format(name=name, price=listOfItems[name]))