class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, id, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = id
        self.scores = scores
    
    def calculate(self):
        a = sum(self.scores) / len(self.scores)
        grade = ''
        if 90 <= a <= 100:grade = 'O'
        elif 80 <= a < 90: grade = 'E'
        elif 70 <= a < 80: grade = 'A'
        elif 55 <= a < 70: grade = 'P'
        elif 40 <= a < 55: grade = 'D'
        else: grade = 'T'
        return grade


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())