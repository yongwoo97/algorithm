a, b = map(int, input().split())
data = list(map(int, input().split()))

from collections import deque
q = deque()
for i in range(1, a+1):
    q.append(i)

count = 0
for i in data:
    while True:
        #print(q, count)
        if q[0] == i:
            q.popleft()
            break
        elif q.index(i) <= len(q) // 2:
            while q[0] != i:
                q.append(q.popleft())
                count += 1
        elif q.index(i) > len(q) // 2:
            while q[0] != i:
                q.appendleft(q.pop())
                count += 1

print(count)
