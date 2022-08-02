import sys
input = sys.stdin.readline
'''
n, m = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

#dfs를 활용한 사이클 검출 알고리즘
minn = float('inf')
visited = [0] * (n+1)
finished = [0] * (n+1)
def dfs(start, c):
    global visited, graph, finished, minn

    #종료 조건을 설정 해야지
    if visited[start]:
        if not finished[start]:
            minn = min(minn, c)
            return True
        return False

    visited[start] = 1

    for node, wei in graph[start]:
        if not visited[node]:
            dfs(node, c + wei)
        elif not finished[node]:
            minn = min(minn, c + wei)

    finished[start] = 1

    return False
if dfs(1, 0):
    print(minn)
else:
    print(-1)
'''

#플로이드 워셜 알고리즘
import sys
input = sys.stdin.readline
INF =int(1e9)
v,e = map(int,input().split())
graph =[[INF for _ in range(v+1)] for _ in range(v+1)]

#자기자신으로 가는 경로는 0 으로 초기화
for i in range(1,v+1):
    graph[i][i] = 0

for i in range(e):
    a,b,c = map(int,input().split())
    graph[a][b]=c

# 3중포문으로 k를 거칠 때의 최단경로 까지 계산
for k in range(1,v+1):
    for a in range(1,v+1):
        for b in range(1,v+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])
# 결과 : 각 노드에서 각 노드 까지의 최단거리 계산
route=[]
temp=INF
for i in range(1,v):
    for j in range(i+1, v+1):
        #i에서 출발해서 i로 돌아오는 최단거리
        temp = min(temp,graph[i][j]+graph[j][i])

if temp ==INF:
    print(-1)
else:
    print(temp)