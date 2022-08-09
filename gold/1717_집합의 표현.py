import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [i for i in range(n+1)]

def find(k):
    global arr
    if k != arr[k]:
        arr[k] = find(arr[k])
    return arr[k]

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        b_jo = find(b)
        c_jo = find(c)
        if b_jo < c_jo:
            #여기서 조상값으로 갱신해야 하는이유가 뭐지?
            #그냥 arr[c] = b_jo로 갱신해야 하는거 아니야? 이상하네
            arr[c_jo] = b_jo
        else:
            arr[b_jo] = c_jo

    else:
        if find(c) == find(b):
            print('YES')
        else:
            print('NO')
#