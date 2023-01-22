#카드 섞는 방법이 있을때
#원하는 카드를 원하는 플레이어에 주고 싶을때 섞어야 하는 최소값을 구해라

#단순 구현인가?
#아니면 다른 알고리즘적 문제가 잇는 것인가?>

import sys
input = sys.stdin.readline
n = int(input())
p = list(map(int, input().split()))
s = list(map(int, input().split()))

#브레이크 포인트를 설정하는게 관건이네
#논리적인 포인트를 설정하는 방법이 있을까? 최소한의 연산으로... 원래 배열과 동일하면 리턴해야겠다


from copy import deepcopy
ref = deepcopy(p)

def rotate(d):
    global s
    temp = [0] * len(d)
    for i in range(len(s)):
        temp[s[i]] = d[i]
    return temp

count = 0
result = []
for i in range(n):
    result.append(i % 3)

if result == p:
    print(0)
else:
    while True:

        p = rotate(p)
        count += 1
        if p == result:
            print(count)
            break
        if p == ref:
            print(-1)
            break