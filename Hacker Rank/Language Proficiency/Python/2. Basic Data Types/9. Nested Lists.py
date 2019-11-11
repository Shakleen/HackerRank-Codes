if __name__ == '__main__':
    students = {}
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in students.keys():
            students[score].append(name)
        else:
            students[score] = [name]

    sortedScores = sorted(students.keys())
    students[sortedScores[1]].sort()
    [print(student) for student in students[sortedScores[1]]]