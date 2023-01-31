import sys, re, heapq
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())
data = []
p1 = re.compile("[A-Z]")
p2 = re.compile("[a-z]")
summ = 0

for e in range(n):
    line = input().rstrip()
    for i in range(n):
        ii = i
        i = line[i]
        if i == '0':
            continue
        else:
            if p1.match(i):
                #heapq.heappush(data, [ord(i) - 38, e, ii])
                data.append([ord(i) - 38, e, ii])
                summ += ord(i) - 38
            elif p2.match(i):
                data.append([ord(i) - 96, e, ii])
                #heapq.heappush(data, [ord(i) - 96, e, ii])
                summ += ord(i) - 96

dp = [i for i in range(n)]

def find(x):
    global dp
    if dp[x] == x:
        return x
    return find(dp[x])

def union(x, y):
    global dp
    xx = find(x)
    yy = find(y)
    if xx > yy:
        dp[xx] = yy
    else:
        dp[yy] = xx
data.sort()
count = 0
#print(data)
while data:
    #z, x, y = heapq.heappop(data)
    z, x, y = data[0]
    data = data[1:]
    if find(x) != find(y):
        count += 1
        summ -= z
        union(x, y)
if n == 0:
    pass
elif count + 1 != n:
    print(-1)
else:
    print(summ)