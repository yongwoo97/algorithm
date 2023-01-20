#일단 재귀를 물어보는 문제 같긴해
#다만 사전순 비교는 스트링으로 바꿔서 해보자
#사전순으로 뒷서는건 어떻게 찾지?

n = int(input())
data = list(map(int, input().split()))
s = int(input())
dif = 0
idx = 0
result = []
from copy import deepcopy
def recur(start, data, k):
    global result, dif, n, s, idx

    if k == s:
        count = 0
        first_appear = 0
        for i in range(n-1):
            if data[i] > data[i+1]:
                count += 1
                first_appear = i
      #  print(count, first_appear, data, dif)
        if count > dif:
            dif = count
            result = deepcopy(data)
       #     print('hello')
       #     print(result)
        elif count == dif:
            if idx > first_appear:
                dif = count
                result = data
                idx = first_appear
        return

    for i in range(start, n-1):
        if data[i] > data[i+1]:
            continue
        data[i], data[i+1] = data[i+1], data[i]
        recur(i + 1, data, k+1)
        data[i], data[i + 1] = data[i + 1], data[i]

recur(0, data, 0)
print(*result)

