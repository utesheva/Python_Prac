from collections import Counter
from timeit import Timer

def count_without(s):
    d = {i:0 for i in s}
    for i in s:
        if i in s:
            d[i] += 1
    return d

def count_with(s):
    return Counter(s)

s = input().split()
print(Timer('count_without(s)', globals = globals()).autorange())
print(Timer('count_with(s)', globals = globals()).autorange())
