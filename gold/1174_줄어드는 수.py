n = int(input())

count = 0
def func(num, step):
    global count, n
    if step == 0:
        count += 1
        if count == n:
            print(num)
        return

    for i in range(10):
        if num and num[-1] > str(i):
            func(num + str(i), step-1)
        elif not num:
            func(num + str(i), step-1)

if n > 1023:
    print(-1)
else:
    for k in range(1, 11):
        func('', k)



