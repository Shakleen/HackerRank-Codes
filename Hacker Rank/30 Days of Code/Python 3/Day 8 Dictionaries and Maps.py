phoneBook = dict()
n = int(input())
for i in range(n):
    name, phoneNo = input().rstrip().rsplit()
    phoneBook[name] = phoneNo

while True:
    try:
        query = input()
        print(
            "{0}={1}".format(query, phoneBook[query])
            if query in phoneBook 
            else 'Not found'
        )
    except EOFError:
        break