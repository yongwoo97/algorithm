n = int(input())

data = [0]
data.append(1)
data.append(2)

for i in range(3, n+1):
    if (data[i-1] + data[i-2]) >= 15746:
        data.append((data[i-1] + data[i-2]) % 15746)
        continue
    else:
        data.append(data[i-1] + data[i-2])
print(data[n] % 15746)
