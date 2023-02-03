n = int(input())
data = [i for i in range(1, n+1)]

summ = 1
for i in range(n):
    if data[i] == 1:
        continue
    summ *= data[i]

    for j in range(i+1, n):
        if data[j] == 1:
            continue
        elif data[j] % data[i] == 0:
            data[j] //= data[i]

print(summ % 987654321)