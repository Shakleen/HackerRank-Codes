import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.X = real
        self.Y = imaginary
        
    def __add__(self, no):
        r = no.X + self.X
        i = no.Y + self.Y
        s = '+' if i >= 0 else ''
        return '{real:.2f}{sign}{imaginary:.2f}i'.format(real=r, sign=s, imaginary=i)
        
    def __sub__(self, no):
        r = self.X - no.X
        i = self.Y - no.Y
        s = '+' if i >= 0 else ''
        return '{real:.2f}{sign}{imaginary:.2f}i'.format(real=r, sign=s, imaginary=i)
        
    def __mul__(self, no):
        r = self.X * no.X - self.Y * no.Y
        i = self.X * no.Y + self.Y * no.X
        s = '+' if i >= 0 else ''
        return '{real:.2f}{sign}{imaginary:.2f}i'.format(real=r, sign=s, imaginary=i)

    def __truediv__(self, no):
        divider = no.X ** 2 + no.Y ** 2
        r = (self.X * no.X + self.Y * no.Y) / divider
        i = (self.Y * no.X - self.X * no.Y) / divider
        s = '+' if i >= 0 else ''
        return '{real:.2f}{sign}{imaginary:.2f}i'.format(real=r, sign=s, imaginary=i)

    def mod(self):
        r = abs(complex(self.X, self.Y))
        return '{real:.2f}{sign}{imaginary:.2f}i'.format(real=r, sign='+', imaginary=0.00)

    def __str__(self):
        if self.Y == 0:
            result = "%.2f+0.00i" % (self.X)
        elif self.X == 0:
            if self.Y >= 0:
                result = "0.00+%.2fi" % (self.Y)
            else:
                result = "0.00-%.2fi" % (abs(self.Y))
        elif self.Y > 0:
            result = "%.2f+%.2fi" % (self.X, self.Y)
        else:
            result = "%.2f-%.2fi" % (self.X, abs(self.Y))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')