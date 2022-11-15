n = int(input())


d = set()
for i in range(1, n+1):
    if n % i == 0:
        a = n // i

        if (a+i) % 2 == 0 and a-i != 0:
            result = (a+i) // 2
            d.add(result)
d = list(d)
d.sort()

if d:
    for i in d:
        print(i)
else:
    print(-1)