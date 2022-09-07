n = int(input())
data = list(map(int, input().split()))
a, c = map(int, input().split())
count = 0
for i in range(n):
    num = data[i]

    mi = num - a
    count += 1
    if mi > 0:
        resi = mi % c
        if resi != 0:
            count += (mi // c) + 1
        else:
            count += (mi // c)
print(count)
