n, m = map(int, input().split())
D = list(map(int, input().split()))
M = list(map(int, input().split()))



def ff(a, b):
    if a == b:
        return a

    if a < b:
        k = a
        #결국엔 이부분에서 시간 단축을 할 수 있는 방법을 찾아야 하는데 음... 어떻게 해야할까? 쉽지 않네
        while k >= int(a ** 0.5):
            if a % k == 0 and b % k == 0:
                return k
            k -= 1

    elif a > b:
        k = b

        while k >= int(b ** 0.5):
            if b % k == 0 and a % k == 0:
                return k
            k -= 1

    return 1


def f(a, b):
    if a % b == 0:
        return a
    elif b % a == 0:
        return b

    goyak = ff(a, b)
    return (a // goyak) * b

start = D[0]
for i in D[1:]:
    start = f(start, i)

maxx = max(M)
minn = min(M)
count = 0
idx = 1
while start * idx <= minn:
    check = True
    for i in M:
        if i % (start * idx) != 0:
            check = False
            break
    if check:
        count += 1

    idx += 1
print(count)
