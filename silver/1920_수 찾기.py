N = int(input())
n1 = list(map(int, input().split()))
n1.sort()

M = int(input())
m1 = list(map(int, input().split()))

def finder(arr, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2

    if arr[mid] == target:
        return 1

    if arr[mid] > target:
        return finder(arr, target, start, mid-1)
    elif arr[mid] < target:
        return finder(arr, target, mid+1, end)

for k in m1:
    print(finder(n1, k, 0, N-1))
