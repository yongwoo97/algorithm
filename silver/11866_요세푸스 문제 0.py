n, k = map(int, input().split())
from collections import deque

q = deque()
for i in range(1, n+1):
    q.append(i)

result = []
i = 0
while q:
    if i == k-1:
        result.append(q.popleft())
        i = 0
    else:
        q.append(q.popleft())
        i += 1


print('<' + ', '.join(list(map(str, result))) + '>')