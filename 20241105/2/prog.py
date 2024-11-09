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

    def __bool__(self):
        return self.__abs__() > 0

    def __lt__(self, other):
        return self.__abs__() < other.__abs__()

    def check_point(self, x, y, pol):
        v1 = (pol.p1[0] - x)*(pol.p2[1] - y) - (pol.p2[0] - x)*(pol.p1[1] - y)
        v2 = (pol.p2[0] - x)*(pol.p3[1] - y) - (pol.p3[0] - x)*(pol.p2[1] - y)
        v3 = (pol.p3[0] - x)*(pol.p1[1] - y) - (pol.p1[0] - x)*(pol.p3[1] - y)
        if (v1 < 0 and v2 < 0 and v3 < 0) or (v1 > 0 and v2 > 0 and v3 > 0):
            return True
        return False

    def __and__(self, other):
        if self.__abs__() == 0 or other.__abs__() == 0:
            return False
        return (self.check_point(*other.p1, self) or self.check_point(*other.p2, self) or self.check_point(*other.p3, self) 
                or self.check_point(*self.p1, other) or self.check_point(*self.p2, other) or self.check_point(*self.p3, other))

    def __contains__(self, other):
        if not other or other == self:
            return True
        return self.check_point(*other.p1, self) and self.check_point(*other.p2, self) and self.check_point(*other.p3, self)

import sys
exec(sys.stdin.read())

