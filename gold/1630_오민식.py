n = int(input())

s = 1
for i in range(n, 1, -1):
    if s % i == 0:
        continue

    start = int(i ** 0.5)
    while start >= 1:
        ss = s

        if i % start == 0:
            right = i // start
            #print(ss, start, right, 'here')
            if ss % start != 0:
                s *= start
            elif ss % start == 0:
                ss //= start
                if ss <= 0:
                    ss = 1
            if ss % right != 0:
                s *= right
        start -= 1
print(s % 987654321)