import math
AB = int(input())
BC = int(input())
AC = (AB * AB + BC * BC) ** 0.5
theta = math.degrees(math.asin(AB/AC))
print('{}°'.format(theta))