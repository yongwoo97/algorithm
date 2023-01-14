import sys
#한 행이 모두 켜졌을 때를 가정하고 최대값을 구한다.
sys.setrecursionlimit(10000)
input = sys.stdin.readline

row, col = map(int, input().split())
data = [list(map(int, list(input().rstrip()))) for _ in range(row)]
k = int(input())

def calc(data):
    global row, col

    result = 0
    for i in range(row):
        if sum(data[i]) == col:
            result += 1

    return result
from copy import deepcopy
def func(data):
    global row, col

    maxx_odd1 = 0
    maxx_odd_count1 = float('inf')
    maxx_even1 = 0
    maxx_even_count1 = float('inf')

    check = False
    for i in range(row):
        count = 0
        d = deepcopy(data)

        for j in range(col):
            if d[i][j] == 1:
                continue
            else:
                for e in range(row):
                    if d[e][j] == 0:
                        d[e][j] = 1
                    else:
                        d[e][j] = 0
                count += 1

        semi_result = calc(d)

        if count % 2 == 0:
            if maxx_even1 < semi_result and k >= count:
                maxx_even1 = semi_result
                maxx_even_count1 = count

        else:
            if maxx_odd1 < semi_result and k >= count:
                maxx_odd1 = semi_result
                maxx_odd_count1 = count
    return [maxx_odd1, maxx_odd_count1, maxx_even1, maxx_even_count1]

l = func(data)
#print(l)
if k == 0:
    print(calc(data))
elif k % 2 == 0:
    print(l[2])
else:
    print(l[0])
