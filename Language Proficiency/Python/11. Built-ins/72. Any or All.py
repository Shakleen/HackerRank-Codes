N = int(input())
numbers = list(map(int, input().split()))
all_pos = [x > 0 for x in numbers]
objective = False

if all(all_pos): 
    any_palindrome = [x - int(str(x)[::-1]) == 0 for x in numbers]
    if any(any_palindrome): 
        objective = True

print(objective)