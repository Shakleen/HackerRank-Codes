class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        maxNo = max(self.__elements)
        minNo = min(self.__elements)
        self.maximumDifference = abs(maxNo - minNo)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)