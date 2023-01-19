n, m = map(int, input().split())

k = n


l = 0
for i in range(1, 11):
    if k - (i * 9 * 10 ** (i-1)) < 0:
        l += k * i
        break
    l += (i * 9 * 10 ** (i-1))
    k -= (9 * 10 ** (i-1))

if m > l:
    print(-1)
else:

    idx = 1
    d = m
    for i in range(1, 11):
        if d > i * (10 ** (i-1)) * 9:
            idx = i + 1
            d -= i * (10 ** (i-1)) * 9
        else:
            break

    semi = d // idx
    residue = d % idx
   # print(semi, residue, d)
    if semi == 0:
        target = 10 ** (idx - 1)
        print(str(target)[residue-1])
    else:
        if residue > 0:
            target = 10 ** (idx-1) + semi
            print(str(target)[residue-1])
        else:
            target = 10 ** (idx-1) + (semi - 1)
            print(str(target)[-1])

