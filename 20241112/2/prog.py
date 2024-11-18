from math import sqrt

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = tuple(p1)
        self.p2 = tuple(p2)
        self.p3 = tuple(p3)

    def __abs__(self):
        d1 = sqrt((self.p1[0] - self.p2[0])**2 + (self.p1[1] - self.p2[1]) ** 2)
        d2 = sqrt((self.p1[0] - self.p3[0])**2 + (self.p1[1] - self.p3[1]) ** 2)
        d3 = sqrt((self.p3[0] - self.p2[0])**2 + (self.p3[1] - self.p2[1]) ** 2)
        if (d1  > d2 + d3) or (d2 > d1 + d3) or (d3 > d1 + d2):
            return 0
        else:
            p = 0.5 * (d1 + d2 + d3)
            s = sqrt(p * (p - d1) * (p - d2) * (p - d3))
            return s if s > 0 else 0

    def check_point(self, x, y, pol):
        v1 = (pol.p1[0] - x)*(pol.p2[1] - y) - (pol.p2[0] - x)*(pol.p1[1] - y)
        v2 = (pol.p2[0] - x)*(pol.p3[1] - y) - (pol.p3[0] - x)*(pol.p2[1] - y)
        v3 = (pol.p3[0] - x)*(pol.p1[1] - y) - (pol.p1[0] - x)*(pol.p3[1] - y)
        if (v1 < 0 and v2 < 0 and v3 < 0) or (v1 > 0 and v2 > 0 and v3 > 0):
            return True
        return False

class InvalidInput(BaseException):
    pass

class BadTriangle(BaseException):
    pass

def triangleSquare(inStr):
    while True:
        try:
            (x1, y1), (x2, y2), (x3, y3)  = eval(inStr)
        except:
            raise InvalidInput
        t = Triangle((x1, y1), (x2, y2), (x3, y3))
        if not t.check_point or abs(t) == 0:
            raise BadTriangle
        else:
            return abs(t)

while True:
    try:
        t = triangleSquare(input())
    except InvalidInput:
        print('Invalid input')
    except BadTriangle:
        print('Not a triangle')
    else:
        print(f'{t:.2f}')
        break
