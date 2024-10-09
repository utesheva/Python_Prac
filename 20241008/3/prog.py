h = 0
gas = 0
liq = 0
w = 0
while s:=input():
    h += 1
    if s.find('.') == -1 and s.find('~') == -1:
        if w > 0: break
        w = s.count('#')
    gas += s.count('.')
    liq += s.count('~')

v = gas + liq

for i in range(w):
    if i == 0 or i == w - 1:
        print('#' * h)
        continue
    if gas > 0:
        print(f'#{'.' * (h - 2)}#')
        gas -= h - 2
    else:
        print(f'#{'~' * (h - 2)}#')
m = max(liq, v - liq)
print(f'{'.' * round(20 * (v - liq) / m):20} {str(v - liq) + '/' + str(v) :>5}')
print(f'{'~' * round(20 * (liq / m)):20} {str(liq) + '/' + str(v):>5}')

