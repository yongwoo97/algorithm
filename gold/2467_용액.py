#이진탐색을 활용한다 왜냐하면 정렬되어 있으니까
'''
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

def search(a, pivot):

    maxx = float('inf')

    start = 0
    end = len(a) - 1

    result = []

    while start <= end:

        mid = (end + start) // 2
        #print(start, end, mid)
        if pivot < 0 and pivot + a[mid] > 0:
            end = mid - 1

        elif pivot < 0 and pivot + a[mid] < 0:
            start = mid + 1

        elif pivot > 0 and pivot + a[mid] < 0:
            start = mid + 1

        elif pivot > 0 and pivot + a[mid] > 0:
            end = mid - 1

        if abs(pivot + a[mid]) < maxx:
            maxx = abs(pivot + a[mid])
            result = [pivot, a[mid], maxx]


    return result

m1 = float('inf')
re = []
for i in range(n//2+1):
    pivot = data[i]
    if pivot < 0:
        ndata = data[i+1:]
    else:
        ndata = data[:i]
    r = search(ndata, pivot)
    if r[2] == 0:
        re = r[:2]
        break
    elif r[2] < m1:
        m1 = r[2]
        re = r[:2]

print(*re)
'''

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))



l = 0
r = n - 1

minn = sys.maxsize
result = []
while l < r:

    if abs(arr[l] + arr[r]) < minn:
        minn = abs(arr[l]  +arr[r])
        result = [arr[l], arr[r]]

    if arr[l] + arr[r] > 0:
        r -= 1
    else:
        l += 1
print(*result)