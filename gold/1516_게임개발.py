import sys
input = sys.stdin.readline

n = int(input())
graph = {i:[] for i in range(1, n+1)}
counter = [0] * (n+1)
degree = [0] * (n+1)
dp = [0] * (n+1)
for e in range(1, n+1):
    line = list(map(int, input().split()))
    for i in range(len(line)):
        if line[i] == -1:
            break
        if i == 0:
            counter[e] = line[i]
            continue
        else:
            degree[e] += 1
            graph[line[i]].append(e)

#print(graph)
#print(degree)
#print(counter)

from collections import deque
def bfs():
    global graph, degree, counter

    q = deque()

    for i in range(1, n+1):
        if degree[i] == 0:
            q.append(i)
            degree[i] = -1
            dp[i] = counter[i]


    while q:
        x = q.popleft()

        for i in graph[x]:
            degree[i] -= 1
            dp[i] = max(dp[i], dp[x] + counter[i])

            if degree[i] == 0:
                q.append(i)


bfs()
for i in dp[1:]:
    print(i)
