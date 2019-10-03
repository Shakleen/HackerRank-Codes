import math
AB = int(input())
BC = int(input())
AC = (AB * AB + BC * BC) ** 0.5
MC = AC / 2
angACB = math.asin(AB/AC)
a = MC * math.sin(angACB)
b = MC * math.sin(90 - angACB)
theta = math.tan(-a/b)
print(round(theta))
# a = BC
# b = AC
# c = AB
# ACB = sin-1((c * sin(ABC)) / b)