n = int(input())

data = []
for _ in range(n):
    line = list(map(int, input().split()))
    if len(line) != n:
        line = line + [0] * (n -len(line))
    data.append(line)

for i in range(1, n):
    for j in range(i+1):
        data[i][j] += max(data[i-1][j], data[i-1][j-1])
print(max(data[-1]))