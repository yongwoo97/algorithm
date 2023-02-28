n, m = map(int, input().split())
data = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    line = list(map(int, input().split()))
    for j in range(1, m+1):
        data[i][j] = line[j-1] + data[i-1][j] + data[i][j-1] - data[i-1][j-1]

maxx = float('-inf')

for i in range(1, n+1):
    for j in range(1, m+1):
        #if i == 1 or j == 1:
        #    maxx = max(maxx, data[i][j])
        #    continue
        for x in range(i, 0, -1):
            for y in range(j, 0, -1):
               # if x == i and y == j:
               #     continue
                maxx = max(maxx, data[i][j] + data[x-1][y-1] - data[i][y-1] - data[x-1][j])
print(maxx)