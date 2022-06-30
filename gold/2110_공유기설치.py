import sys
input = sys.stdin.readline
'''
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
'''
n, c = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

array.sort()


def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = array[0]
        count = 1

        for i in range(1, len(array)):
            if array[i] >= current + mid:
                count += 1
                current = array[i]

        if count >= c:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1


start = 1
end = array[-1] - array[0]
answer = 0

binary_search(array, start, end)
print(answer)

