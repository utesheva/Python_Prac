from math import *
w, h = eval(input())
a, b = eval(input())

screen = [[' '] * w for i in range(h)]
def scale(a, b, A, B, x):
    return (B - A) * (x - a)/(b - a) + A

def show(screen):
    print('\n'.join(["".join(s) for s in screen]))

for i in range(w):
    x = scale(0, w - 1, a, b, i)
    y = sin(x)
    shift = round(scale(-1, 1, 0, h - 1, y))
    screen[shift][i] = '*'
show(screen)
