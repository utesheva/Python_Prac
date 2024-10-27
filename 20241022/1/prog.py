import sys

def fib(m, n):
    prev = 1
    cur = 1
    if m == 0:
        yield prev
        yield cur
    elif m == 1:
        yield cur
    for i in range(2, m + n):
        temp = cur
        cur += prev
        prev = temp
        if i >= m:
            yield cur

exec(sys.stdin.read())
