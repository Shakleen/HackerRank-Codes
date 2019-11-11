from collections import namedtuple
student = namedtuple('student', 'ID, MARKS, NAME, CLASS')
N = int(input())
order = input().split()
form = "s = student({o[0]} = '{v[0]}', {o[1]} = '{v[1]}', {o[2]} = '{v[2]}', {o[3]} = '{v[3]}')"
total = 0

for i in range(N):
    values = list(input().split())
    exec(form.format(o=order, v=values))
    total += int(s.MARKS)

print(total / N)