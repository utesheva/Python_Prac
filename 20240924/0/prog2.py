s1 = list(range(5, 16))
#s2 = [chr(i) for i in range(ord('a'), ord('k') + 1)]
s2 = list('abcdefghijk')
s1[4:8] = s2[-5:]
print(s1)
