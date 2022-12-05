n = int(input())
data = list(map(int, input().split()))

count = 0
def func(a, i):
    global data, count, n

    if a > 20:
        return
    elif a < 0:
        return

    if i == n - 2:
        if a + data[i] == data[n-1]:
            count += 1
            return
        elif a - data[i] == data[n-1]:
            count += 1
            return
        else:
            return


    func(a + data[i], i + 1)
    func(a - data[i], i + 1)

func(0, 0)
print(count)