s = list()
for i in eval(input()):
    s.append([i*i % 100, i])
for i in range(len(s)):
    for j in range(i+1, len(s)):
        if s[i][0] > s[j][0]:
            s[i], s[j] = s[j], s[i]
new_s = [i[1] for i in s]
print(new_s)
