import sys
input = sys.stdin.readline

v, e = map(int, input().split())
graph = {i:[] for i in range(1, v+1)}

for _ in range(e):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)

check = [0] * v
result = []

def dfs(data, start):
    global check, result

    if check[start-1]:
        return

    stack = []
    stack.append(start)

    while stack:
        print(stack, result)
        if check[stack[-1]-1] == 0:
            check[stack[-1]-1] = 1

            for i in data[stack[-1]]:
                if check[i-1]
print(graph)
for i in range(1, v+1):
    dfs(graph, i)

print(result)
