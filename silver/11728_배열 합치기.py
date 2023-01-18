import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
a = deque(map(int, input().split()))
b = deque(map(int, input().split()))

arr =[]
i = 0
j = 0

while True:
    if not a and not b:
        break

    if a and not b:
        arr = arr + list(a)
        break
    elif not a and b:
        arr = arr + list(b)
        break

    if a[0] > b[0]:
        arr.append(b.popleft())
       # b = b[1:]
    else:
        arr.append(a.popleft())
      #  a = a[1:]
  #  print(arr)
print(*arr)