def rbin(r, n, args = [1]):
    if n <= 1: 
        print(*args, sep = '')
        return
    rbin(0, n - 1, args + [0])
    rbin(1, n - 1, args + [1])
