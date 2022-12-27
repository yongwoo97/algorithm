import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
n = int(input())
graph = {i:[] for i in range(1, n+1)}
dp = [[0, 0] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
#이게 왜 양방향 트리여야 하지? 그냥 그래프인데, 사이클이 존재하지 않는다고 해야하나
#print(graph)
visited = [0] * (n+1)
def dfs(start):
    global n, graph, dp, visited
    visited[start] = 1
    if len(graph[start]) == 0:
        dp[start][0] = 0
        dp[start][1] = 1
        return

    for i in graph[start]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)
            dp[start][0] += dp[i][1]
            dp[start][1] += min(dp[i][0], dp[i][1])
    #이 아랫줄의 의미는 무엇이지?
    #자기 자신이 얼리어답터니까 추가해줘야겠지
    dp[start][1] += 1
dfs(1)
#print(dp)
print(min(dp[1][0], dp[1][1]))