n = int(input())
from collections import deque
for _ in range(n):
    a, b = map(int, input().split())

    k = deque()
    data = list(map(int, input().split()))


    for i, j in enumerate(data):
        k.append((i, j))

    count = 0
    while k:

        m = max(k, key=lambda x: x[1])[1]
        p = k.popleft()
        if p[0] == b and p[1] >= m:
            count += 1
            print(count)
            break
        elif p[1] >= m:
            count += 1
            continue
        else:
            k.append(p)
