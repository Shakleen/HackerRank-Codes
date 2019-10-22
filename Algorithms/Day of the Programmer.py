year = int(input())

def isLeapYear(year):
    if year >= 1918:
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    return year % 4 == 0

day = 256
feb = (28 if year != 1918 else 15) + isLeapYear(year)
calendar = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for length in calendar:
    day -= length
    if day < 30: break

print('{}.09.{}'.format(day, year))