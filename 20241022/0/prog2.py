def travel(n):
    yield from 'по кочкам' for i in range(n)
    return "и в яму"
