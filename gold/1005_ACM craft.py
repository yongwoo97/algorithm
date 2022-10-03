#역순으로 그래프만들고 bfs 탐색후 레벨별로 맥스값저장하고 합계출력
import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    data = list(map(int, input().split()))
    graph = {i:[] for i in range(a)}
    degree = [0] * a
    dp = [0] * a
    for _ in range(b):
        x, y = map(int, input().split())
        graph[x-1].append(y-1)
        degree[y-1] += 1

    target = int(input()) - 1

    q = deque()

    for i in range(a):
        if degree[i] == 0:
            q.append(i)
            dp[i] += data[i]
            degree[i] = -1




    #print(degree)
    while q:
      #  print(dp)
        x = q.popleft()

        for i in graph[x]:
            dp[i] = max(dp[x] + data[i], dp[i])
            degree[i] -= 1

        for i in range(a):
            if degree[i] == 0:
                q.append(i)
                degree[i] = -1
    #print(dp)
    print(dp[target])



