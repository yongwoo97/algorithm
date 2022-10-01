import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

K = [list(map(int, input().split())) for _ in range(k)]
#print(K)
from copy import deepcopy
def permute(arr, t):

    if t <= 1:
        semi = []
        for i in arr:
            semi.append([i])
        return semi


    result = []
    for i in range(len(arr)):
        arr1 = deepcopy(arr)
        del arr1[i]
        semi = permute(arr1, t-1)
        for j in semi:
            result.append([arr[i]] + j)
    return result

def rotate(r, c, r1, c1):
    #첫셀만 기억하고 나머지는 돌리면 되잖아.
    global data1
    left = r
    right = c

    lleft = r1
    rright = c1

    start = data1[left][right]
    #아래에서 위로
    for i in range(left+1, lleft + 1):
         data1[i-1][right] = data1[i][right]
    #오른쪽에서 왼쪽
    for i in range(right+1, rright + 1):
        data1[lleft][i-1] = data1[lleft][i]
    #위에서 아래
    for i in range(lleft-1, left-1, -1):
        data1[i+1][rright] = data1[i][rright]
    #왼쪽에서 오른쪽
    for i in range(rright-1, right-1, -1):
        data1[left][i+1] = data1[left][i]
    data1[left][right+1] = start

# width = r + s - (r - s) + 1
# lefnth = c + s - (c - s) + 1
p = permute(K, len(K))

minn = float('inf')
for i in p:
    data1 = deepcopy(data)
   # print(i)
    for e in i:
      #  print(e)
       # ss = (e[2] * 2 + 1)

      #  print(e)
        for x in range(1, e[2] + 1):
            sx = e[0] - x - 1
            sy = e[1] - x - 1
            ex = e[0] + x - 1
            ey = e[1] + x - 1
          #  print(sx, sy, ex, ey)
            rotate(sx, sy, ex, ey)


    for q in data1:
        minn = min(minn, sum(q))

print(minn)
