m, n = eval(input())
'''
s = []
for i in range(m, n+1):
    for j in range(2, i):
        print(i, j, i % j)
        if i % j == 0:
            break
    else:
        s.append(i)
print(s)
'''
print([i for i in range(m, n) if  i != 1 and all([i % j != 0 for j in range(2, i)])])
