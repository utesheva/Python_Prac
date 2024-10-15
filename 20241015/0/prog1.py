import string
import timeit

def wov_cons(st):
    g = {'a', 'e', 'u', 'y', 'o', 'i'}
    s = set(string.ascii_lowercase) - g
    st = set(st)
    return len(st & g), len(st & s)

st = input()
T = timeit.Timer("wov_cons", globals = globals())
print(T.autorange())
