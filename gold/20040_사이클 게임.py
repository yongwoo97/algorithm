#union find로 하면 빨리 할 수 있을것 같은데?
#
import sys
input = sys.stdin.readline

n, m = map(int ,input().split())
arr = [i for i in range(n+1)]

def find(x):
    if arr[x] == x:
        return x
    return find(arr[x])

def union(x, y):
    nx = find(x)
    ny = find(y)

    if nx > ny:
        arr[nx] = ny
    else:
        arr[ny] = nx

for k in range(m):
    a, b = map(int, input().split())
    fa = find(a)
    fb = find(b)

    if fa == fb:
        print(k+1)
        exit()
    else:
        union(fa, fb)
print(0)