from decimal import *

def esum(N, one):
    s = one
    pred = one
    for i in range(1, N):
        pred *= i
        s += one/pred
    return s
