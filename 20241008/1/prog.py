from fractions import *
s, w = 0, 0
pow_A, pow_B = 0, 0
c_A, c_B = list(), list()
for n,i in enumerate(input().split(', ')):
    if n == 0:
        s = Fraction(i)
    elif n == 1:
        w = Fraction(i)
    elif n == 2:
        pow_A = Fraction(i)
    elif n > 2 and n <= 2 + pow_A + 1:
        c_A.append(Fraction(i))
    elif n == 2 + pow_A + 2:
        pow_B = Fraction(i)
    else:
        c_B.append(Fraction(i))
A = sum([i * (s ** (pow_A - n)) for n, i in enumerate(c_A)])
B = sum([i * (s ** (pow_B - n)) for n, i in enumerate(c_B)])
if B == 0:
    print(False)
elif A / B == w:
    print(True)
else:
    print(False)
