#조금 재미있는 문제네
#어떻게 풀어야 할까?
#2022.12.28 다시 고민해본다.
#와 이게 set을 활용한 브루트 포스였다니...
#비트 마스킹을 활용할 수 있는 방법이 있을까?

from collections import deque

n, k = map(int, input().split())
l = list(input().split())

visited = set("".join(l))
q = deque()
q.append(["".join(l), 0])
ans = -1

from copy import deepcopy
while q:
    word, cnt = q.popleft()
    temp = list(word)

    if temp == sorted(temp):
        ans = cnt
        break

    for i in range(n-k+1):
        new = deepcopy(temp[i:i+k])
        new.reverse()

        new_word = temp[:i] + new + temp[i+k:]
        newstring = "".join(new_word)

        if newstring not in visited:
            visited.add(newstring)
            q.append([newstring, cnt + 1])
print(ans)