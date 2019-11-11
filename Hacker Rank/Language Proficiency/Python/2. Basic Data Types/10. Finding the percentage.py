if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = sum(scores) / 3
    query_name = input()

    print('{:.2f}'.format(student_marks[query_name]))
