returnDate = list(map(int, input().rstrip().rsplit()))
expectedDate = list(map(int, input().rstrip().rsplit()))
fine = 0
if expectedDate[2] >= returnDate[2]:
    if expectedDate[1] >= returnDate[1]:
        if expectedDate[0] < returnDate[0] and expectedDate[1] == returnDate[1]:
            fine = 15 * (returnDate[0] - expectedDate[0])
    elif expectedDate[2] == returnDate[2]:
        fine = 500 * (returnDate[1] - expectedDate[1])
else:
    fine = 10000

print(int(fine))