n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
data = sorted(data, key = lambda x : (x[0], x[1]))

count = 0
cur = 0
import math
for s, e in data:
    if e < cur:
        continue
    if s > cur:
        cur = s

    dist = e - cur
    remain = 1
    if dist % n == 0:
        remain = 0

    semi = dist // n + remain

    count += semi
    cur += (semi * n)

    #print(semi, cur)
print(count)
#print(data)
#무슨 반례가 있을까?
#아무리 봐도 예외가 없는 알고리즘인데...
#print(math.ceil(1.0))
#아래 코드랑 도대체 무슨 차이야
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
pool = [list(map(int, input().split())) for _ in range(n)]
pool.sort(key=lambda x: x[0])
plank = pool[0][0]
total_count = 0
for start, end in pool:
    if plank > end:
        continue
    elif plank < start:
        plank = start
    dist = end - plank
    remainder = 1
    if dist % l == 0:
        remainder = 0
    count = dist // l + remainder
    plank += count * l
    total_count += count
print(total_count)