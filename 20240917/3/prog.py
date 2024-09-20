n = int(input())
i = n
while i <= n + 2: 
    j = n
    while j <= n + 2:
        temp = i * j
        summary = 0
        while temp > 0:
            summary += temp % 10
            temp //= 10
        if summary == 6:
            print(i, "*", j, "= :=)", end = ' ')
        else:
            print(i, "*", j, "=", i * j, end = ' ')
        j += 1
    i += 1
    print()
