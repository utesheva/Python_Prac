class Omnibus:
    def __setattr__(self, attr, n):
        if attr in dir(Omnibus):
            setattr(Omnibus, attr, getattr(Omnibus, attr) + 1)
        else:
            setattr(Omnibus, attr, 1)

    def __getattribute__(self, attr):
        return getattr(Omnibus, attr)

    def __delattr__(self, attr):
        if attr in dir(Omnibus):
            setattr(Omnibus, attr, getattr(Omnibus, attr) - 1)

a, b, c = Omnibus(), Omnibus(), Omnibus()
del a.random
a.i = a.j = a.k = True
b.j = b.k = b.n = False
c.k = c.n = c.m = hex
print(a.i, a.j, a.k, b.j, b.k, b.n, c.k, c.n, c.m)
del a.k, b.n, c.m
print(a.i, a.j, b.j, b.k, c.k, c.n)
del a.k, c.m
print(a.i, a.j, b.j, b.k, c.k, c.n)
a.k = b.i = c.m = 777
print(a.i, a.j, a.k, b.j, b.k, c.k, c.n, c.m)
