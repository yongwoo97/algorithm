n = int(input())
from collections import deque
data = deque()
for i in range(1, n+1):
    data.append(i)
def action(f):
    while len(f) != 1 and len(f) > 1:
        f.popleft()
        if len(f) == 1:
            break
        last = f.popleft()
        data.append(last)
    return f[0]

print(action(data))

