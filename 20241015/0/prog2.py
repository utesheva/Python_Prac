d = dict()
for i in input().split(' '):
    if i in list(d.keys()):
        d[i] += 1
    else:
        d[i] = 1
print(d)

