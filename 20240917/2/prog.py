summary = 0
n = int(input())
while n > 0:
    summary += n
    if summary > 21:
        print(summary)
        break
    n = int(input())
else:
    print(n)
