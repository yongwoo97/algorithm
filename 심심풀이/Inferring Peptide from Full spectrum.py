idx = 0
p = 0
data = []
while True:
    line = input().strip()
    if not line:
        break


    line = float(line)
    if idx == 0:
        p = line
        idx += 1
        continue
    data.append(line)
n = len(data)// 2
data.sort()

graph = []
print(n)
for i in range(n):
    graph.append([data[i], data[len(data) - 1 - i]])
print(graph)
def recur(d, cur, dd):
    global n
    if cur == n:
        print(dd)
        dd.sort()
        for j in range(1, len(dd)):
            print(dd[j] - dd[j-1], end = ' ')
        print()
        return

    for i in range(2):
        recur(d, cur + 1, dd + [d[cur][i]])

recur(graph, 0, [])