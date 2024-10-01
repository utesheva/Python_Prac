def MINF(*args):
    def g(x):
        return min([i(x) for i in args])
    return g
