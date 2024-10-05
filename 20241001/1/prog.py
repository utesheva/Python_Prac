def Pareto(*arg):
    answ = tuple()
    for x in arg:
        for y in arg:
            if x != y and (x[0] <= y[0] and x[1] <= y[1] and (x[0] < y[0] or x[1]< y[1])):
                break
        else:
            answ += ((x),)
    return answ
print(Pareto(*eval(input())))
