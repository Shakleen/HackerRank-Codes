n = int(input())

for i in range(n):
    grade = int(input())
    rounded_grade = grade

    if grade >= 38:
        next_multiple = ((grade // 5) + 1) * 5
        
        if next_multiple - grade < 3:
            rounded_grade = next_multiple
    
    print(rounded_grade)