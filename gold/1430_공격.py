import sys
input = sys.stdin.readline

data = []
n, r, d, x, y = map(int, input().split())
for _ in range(n):
    a, b = map(int, input().split())
    data.append([a, b])


def distance(x1, y1, x2, y2):
    result = ((abs(x1 - x2) ** 2) + (abs(y1 - y2) ** 2)) ** 0.5
    return result
from collections import deque
def bfs():
    global data, n, r, d, x, y
    dp = [0] * n
    q = deque()
    count = 0
    for i in range(n):
        xx, yy = data[i]
        dis = distance(xx, yy, x, y)
        if dis <= r:
            q.append([xx, yy, 0])
            count += d
            dp[i] = 1
  #  print(q)
    while q:
        x1, y1, dd = q.popleft()

        for i in range(n):
            if dp[i] == 0:
                dist = distance(x1, y1, data[i][0], data[i][1])
                if dist <= r:
                    dp[i] =1
                   # print(d * (0.5 ** (dd + 1)))
                    count += d * (0.5 ** (dd + 1))
                    q.append([data[i][0], data[i][1], dd + 1])

    return count

print(bfs())