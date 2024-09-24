s = []
while (a := input()):
    s.append(eval(a))
if all([len(i) == len(s) for i in s]):
    for i in range(len(s)):
        for j in range(i+1):
            s[i][j], s[j][i] = s[j][i], s[i][j]
    print(s)
else:
    print('not square')     
