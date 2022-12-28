#투포인터 문제는 아닌것 같고 그냥 단순 구현인가?
#그냥 투포인터 문제네
#아예 애초에 문제를 잘못 이해했다. 그냥 처음에 돌면서
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
pizza = list(map(int, input().split()))

minn = data[0]
for i in range(1, n):
    if data[i] >= minn:
        data[i] = minn
    else:
        minn = data[i]

data.reverse()

count = 0
pizza_idx = 0
data_idx = 0
#result = 0
while pizza_idx < m and data_idx < n:
    if data[data_idx] >= pizza[pizza_idx]:
        count = data_idx
        pizza_idx += 1
        data_idx += 1
    else:
        data_idx += 1
#print(count)
if pizza_idx < m:
    print(0)
else:
    print(n - count)