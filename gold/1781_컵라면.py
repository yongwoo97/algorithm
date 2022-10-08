import sys, heapq
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(arr, (a, b))

cur = 1
result = 0
minn = []

while arr:
    t = heapq.heappop(arr)
    result += t[1]
    heapq.heappush(minn, t[1])

    while arr and arr[0][0] == cur:
        temp = heapq.heappop(arr)
        if minn[0] < temp[1]:
            p = heapq.heappop(minn)
            result -= p
            heapq.heappush(minn, temp[1])
            result += temp[1]
    cur += 1

if result >= 2**31:
    print(2**31)
else:
    print(result)
