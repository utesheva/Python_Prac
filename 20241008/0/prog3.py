from math import *
w, h = eval(input())
a, b = eval(input())

def scale(a, b, A, B, x):
    return (B - A) * (x - a)/(b - a) + A
for i in range(h):
    x = scale(0, h - 1, a, b, i)
    y = sin(x)
    shift = round(scale(-1, 1, 0, w - 1, y))
    print(' ' * shift, '*')
