from math import *
def Calc(s, t, u):
    def f(x):
        def def_s(x):
            return eval(s)
        def def_t(x):
            return eval(t)
        def def_u(x, y):
            return eval(u)
        return def_u(def_s(x), def_t(x))
    return f
s, t, u = eval(input())
x = eval(input())
print(Calc(s, t, u)(x))
