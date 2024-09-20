n = int(input())
a, b, c = 0, 0, 0
sign = ['-', '+']
if n % 25 == 0 and n % 2 == 0: a = 1
if n % 2 != 0 and n % 25 == 0: b = 1
if n % 8 == 0: c = 1
print('A', sign[a], 'B', sign[b], 'C', sign[c])
