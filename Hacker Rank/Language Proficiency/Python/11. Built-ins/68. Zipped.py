N, X = map(int, input().split())
marks = []

for i in range(X):
    marks.append(list(map(float, input().split())))

for mark in zip(*marks):
    print(sum(mark) / len(mark))