import sys
input = sys.stdin.readline

def bst(arr, target, i, j):
    # 빈 배열이면 -1 리턴
    if not arr:
        return -1
    # j가 i 보다 작을때
    if j < i:
        return i

    mid = (i + j) // 2
    if target == arr[mid]:
        return mid
    elif target > arr[mid]:
        return bst(arr, target, mid+1, j)
    else:
        return bst(arr, target, i, mid-1)




n = int(input())
data = list(map(int, input().split()))

a = []

for i in range(n):
    t = data[i]
    idx = bst(a, t, 0, len(a)-1)

    if idx == -1:
        a.append(t)
    elif idx > len(a) - 1:
        a.append(t)
    else:
        a[idx] = t
print(len(a))
