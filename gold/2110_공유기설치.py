import sys
input = sys.stdin.readline
n, k = map(int, input().split())
data = [int(input().rstrip()) for _ in range(n)]
data.sort()

mmax = len(data) - 1
mmin = 0


def func(d, start, end):
    mid = (start + end) // 2

    if start == mid:
        return d[end] - d[start]

    left = d[mid] - d[start]
    right = d[end] - d[mid]

    return min(left, right)


result = -1
for i in range(k-2):
    mid = (mmax - mmin) // 2
    if i == k - 3:
        result = min(data[mid] - data[mmin], data[mmax] - data[mid])
        break
    lef = func(data, mmin, mid)
    rig = func(data, mid, mmax)
    if lef > rig:
        mmax = mid
        result = lef
    else:
        mmin = mid
        result = rig

print(result)

