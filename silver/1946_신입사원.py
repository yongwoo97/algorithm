import sys
input = sys.stdin.readline
n = int(input())
#import heapq
for _ in range(n):
    k = int(input())
    data = []
    for _ in range(k):
        a, b = map(int, input().split())
        data.append([a, b])
    data.sort()
    count = 0
    minn_2 = float('inf')
    for i in range(k):
        if i == 0:
            count += 1
            minn_2 = data[i][1]

        else:
            if data[i][1] < minn_2:
                minn_2 = data[i][1]
                count += 1
    print(count)