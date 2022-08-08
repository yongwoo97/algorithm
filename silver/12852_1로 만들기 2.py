n = int(input())

'''
cnt = 0

#(method, cnt)
#bfs가 아니라 dfs로 구현해야하나? 그래서 백트래킹하면서 찾아내야 하는것같네
#dfs로 길이값이 최소로 가지는 것으로 return 하게 만들어야겠다.


def dfs(k):
    if k == 1:
        return [1]

    r = []
    for i in range(3):
        if i == 0:
            if k % 3 == 0:
                semi1 = dfs(k // 3)
                r.append(semi1)
                continue
        elif i == 1:
            if k % 2 == 0:
                semi2 = dfs(k // 2)
                r.append(semi2)
                continue
        else:
            semi3 = dfs(k-1)
            r.append(semi3)

    r.sort(key=len)



    return [k] + r[0]
re = dfs(n)
print(len(re)-1)
print(*re)


#dfs로 푸니까 시간 초과가 나네 그럼 bfs로 풀어야하나? 흠...
#백트래킹은 어떻게 하지?
#뭔가 거의 알것 같으면서도 쉬운문제는 아니다.
#.. .
from collections import deque
import heapq
from copy import deepcopy
q = []
heapq.heappush(q, [0, n, [n]])
while q:
    cnt, target, arr = heapq.heappop(q)

    if target == 1:
        print(cnt)
        print(*arr)
        break

    for i in range(3):
        if i == 0:
            if target % 3 == 0:
                arr1 = deepcopy(arr)
                arr1.append(target//3)
                heapq.heappush(q, [cnt + 1, target//3, arr1])
        elif i == 1:
            if target % 2 == 0:
                arr2 = deepcopy(arr)
                arr2.append(target//2)
                heapq.heappush(q, [cnt + 1, target // 2, arr2])
        else:
            arr3 = deepcopy(arr)
            arr3.append(target-1)
            heapq.heappush(q, [cnt + 1, target - 1, arr3])
'''

from collections import deque


L = [0]*(n+1)
queue = deque([1])

while queue:
    k = queue.popleft()
    if k + 1 == n or 2*k == n or 3*k == n:
        L[n] = k
        break
    if 3*k < n and not L[3*k]:
        queue.append(3*k)
        L[3*k] = k
    if 2*k < n and not L[2*k]:
        queue.append(2*k)
        L[2*k] = k
    if k+1 < n and not L[k+1]:
        queue.append(k+1)
        L[k+1] = k

ans = [n]
while ans[-1] != 1:
    bef = ans[-1]
    ans.append(L[bef])

print(len(ans)-1)
print(*ans)