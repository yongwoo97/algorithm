check = [0] * 10001
arr = [i for i in range(10001)]

def func(n):
    s = str(n)
    result = n
    for i in s:
        result += int(i)

    return result

for i in arr:
    #if check[i]:
    #    continue
    r = func(i)
    if r <= 10000:
        check[r] = 1

for i in range(10001):
    if not check[i]:
        print(i)

