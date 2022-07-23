import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = {i:[] for i in range(1, n+1)}

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

dp = [[float('inf')] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 0

for i in graph:
    for j in graph[i]:
        a, b = j
        if dp[i-1][a-1] > b:
            dp[i-1][a-1] = b

#for i in dp:
#    print(*i)
#print()
def floid(fix, start):
    global graph, dp

    if fix == start:
        return

    for i in graph[start]:
        next_node, weight = i
        if dp[fix-1][next_node-1] < dp[fix-1][start-1] + weight:
            continue

        if dp[fix-1][next_node-1] > dp[fix-1][start-1] + weight:
            dp[fix-1][next_node-1] = dp[fix-1][start-1] + weight
            floid(fix, next_node)


for i in range(1, n+1):
    for j in range(1, n+1):
        floid(i, j)

for i in range(n):
    for j in range(n):
        if dp[i][j] == float('inf'):
            dp[i][j] = 0

for i in dp:
    print(*i)