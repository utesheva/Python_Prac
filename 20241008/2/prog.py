from math import *
W, H, A, B, f = input().split()
W, H, A, B = int(W), int(H), int(A), int(B), 
screen = [[' '] * W for i in range(H)]


def scale(a, b, A, B, x):
    return (B - A) * (x - a)/(b - a) + A


def show(screen):
    print('\n'.join(["".join(s) for s in screen]))


min_y = min([eval(f) for x in range(A, B + 1)])
max_y = max([eval(f) for x in range(A, B + 1)])
for i in range(W):
    x = scale(0, W - 1, A, B, i)
    y = eval(f)
    shift = round(scale(min_y, max_y, 0, H - 1, y))
    screen[H - shift - 1][i] = '*'
show(screen)

for i in range(H):
    for j in range(W):

