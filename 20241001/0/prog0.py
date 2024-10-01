# распаковка
def fun(a, b, c):
    print(a, b, c)
fun(*range(5, 20, 6))

# запаковка
def fun1(a, *args):
    print(a, args)
fun1(1, 3, 'fsdfd')


def fun2(a, defl = 123, *args):
    print(a, defl, args)
fun(1, 2, 3)

