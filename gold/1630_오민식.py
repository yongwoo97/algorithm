n = int(input())
data = [i for i in range(1, n+1)]
data = [1] + data
summ = 1
for i in range(1, n+1):
    if data[i] == 1:
        continue
    summ *= data[i]

    for j in range(2, n+1):
        next = i * j
        if next > n:
            break
        elif data[next] == 1:
            continue
        elif data[next] % data[i] == 0:
            data[next] //= data[i]
#print(data)
print(summ % 987654321)