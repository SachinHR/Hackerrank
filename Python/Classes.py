# Problem 1 : Classes: Dealing with Complex Numbers

#Solution 1
import math
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = float(real)
        self.imaginary = float(imaginary)

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real, imaginary)

    def conj(self):
        return Complex(self.real, -self.imaginary)

    def __truediv__(self, no):
        if no.imaginary == 0:
            return Complex(self.real / no.real, self.imaginary / no.real)
        else:
            return (self * no.conj()) / (no * no.conj())

    def mod(self):
        squared = (self * self.conj()).real
        return Complex(math.sqrt(squared),0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
____________________________________________________________________________________________________________________________________________
# Problem 2 : Class 2 - Find the Torsional Angle

#Solution 1
import math
class Points(object):
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    def __sub__(self, no):
        return  Points((self.x-no.x),(self.y-no.y),(self.z-no.z))

    def dot(self, no):
        return (self.x*no.x)+(self.y*no.y)+(self.z*no.z)

    def cross(self, no):
        return Points((self.y*no.z-self.z*no.y),(self.z*no.x-self.x*no.z),(self.x*no.y-self.y*no.x))
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
