n = int(input())
data = list(map(int, input().split()))
k = int(input())

tree = {i:[] for i in range(n)}

start = -1
for i in range(n):
    if data[i] == -1:
        start = i
        continue
    tree[data[i]].append(i)

count = 0
def dfs(t, root):
    global count
    if not t[root]:
        count += 1
        return
    for i in t[root]:
        dfs(t,i)



if k == start:
    print(0)
else:
    tree[data[k]].remove(k)
    #print(tree)
    dfs(tree, start)
    print(count)