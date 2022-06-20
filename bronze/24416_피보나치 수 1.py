
n = int(input())

code1 = 0
def f1(k):
    global code1
    if k == 1 or k == 2:
        code1 += 1
        return 1

    return f1(k-1) + f1(k-2)

code2 = 0
def f2(k):
    data = [1, 1]
    global code2

    if k == 1 or k == 2:
        return data[k]


    for i in range(2, k):
        data.append(data[i-1] + data[i-2])
        code2 += 1

    return data[-1]
f1(n)
f2(n)
print(code1, code2)