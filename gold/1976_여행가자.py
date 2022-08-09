#union find로 한번 풀어볼까?
#어떻게 해야하지?
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
go = list(map(int, input().split()))

arr = [i for i in range(n+1)]
def find(k):
    if k != arr[k]:
        arr[k] = find(arr[k])
    return arr[k]

def union(a, b):
    a_josang = find(a)
    b_josang = find(b)

    if a_josang < b_josang:
        arr[b_josang] = a_josang
    else:
        arr[a_josang] = b_josang

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if i >= j:
            continue
        if graph[i][j] == 1:
            union(i+1, j+1)

root = 0
check = False
for i in range(len(go)):
    if i == 0:
        root = find(go[i])
    else:
        if find(go[i]) != root:
            check = True
if check:
    print('NO')
else:
    print('YES')