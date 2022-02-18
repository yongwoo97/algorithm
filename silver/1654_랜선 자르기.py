n, m = map(int, input().split())
pre = [int(input()) for _ in range(n)]
pre.sort()

def calc(k, arr):
    total = 0
    for i in arr:
        total += i // k

    return total

def binary(target, arr, start, end):
    if start > end:
        return end
    mid = (start + end) // 2
    #if mid == 0:
    #    return arr[start]
    if calc(mid, arr) >= target:
        return binary(target, arr, mid + 1, end)
    else:
        return binary(target, arr, start, mid-1)


print(binary(m, pre, 1, pre[-1]))
