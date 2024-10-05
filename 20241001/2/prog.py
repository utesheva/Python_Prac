def subtract(a, b):
    if isinstance(a, int) or isinstance(a, float) or isinstance(a, complex):
        return a - b
    else:
        res = list()
        for i in a:
            if i not in b:
                res.append(i)
        return type(a)(res)
a, b = eval(input())
print(subtract(a,b))
