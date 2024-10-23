from itertools import *
n = int(input())
if n // 3 < 1:
    exit()
tor = ["TOR"] * (n // 3) + ['T', 'O', 'R']
print(', '.join(sorted([''.join(j) for j in set(
    filter(lambda x: sum([len(i) for i in x]) == n,\
           permutations(tor, n//3  + n - (n // 3) * 3)))])))
