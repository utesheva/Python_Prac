import string
g = {'a', 'e', 'u', 'y', 'o', 'i'}
s = set(string.ascii_lowercase) - g
st = set(input())
print(len(st & g))
print(len(st & s))
