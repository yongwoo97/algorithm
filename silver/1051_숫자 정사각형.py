import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = [list(map(int, list(input().rstrip()))) for _ in range(n)]


real_maxx = 1
for i in range(n):
    for j in range(m):
        maxx = 1
        stand = data[i][j]
        for k in range(1, 50):
            if i + k >= n or j + k >= m:
                break
            else:
                if data[i+k][j] == stand and data[i][j+k] == stand and data[i+k][j+k] == stand:
                    maxx = (k+1) ** 2

        real_maxx = max(real_maxx, maxx)
print(real_maxx)