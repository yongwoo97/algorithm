import sys
input = sys.stdin.readline
n = int(input())
data1 = list(input().rstrip())
for i in range(n):
    if i % 2 == 0:
        data1[i] = int(data1[i])

def cal(arr):
    s = arr[0]
    op = ''

    for i in range(1, len(arr)):
        if i % 2 == 1:
            op = arr[i]
        else:
            if op == '+':
                s += arr[i]
            elif op == '-':
                s -= arr[i]
            else:
                s *= arr[i]
    return s

def reduce(arr):
    global data1

    final = []

    i = 0
    while i < len(data1):
        #내가 짯는데 아래 의미를 이해할 수 가 없네.
        if i in arr:
            x = final.pop()
            if data1[i] == '+':
                mid = x + data1[i+1]
            elif data1[i] == '-':
                mid = x - data1[i+1]
            else:
                mid = x * data1[i+1]
            final.append(mid)
            i += 2
        else:
            final.append(data1[i])
            i += 1

    return cal(final)

result = float('-inf')
def dfs(start, pre):
    global result

    if start >= len(data1) - 5:

        result = max(result, reduce(pre))
       # print(pre, reduce(pre))
        return

    for e in range(start + 4, len(data1), 2):
        dfs(e, pre + [e])
    result = max(result, reduce(pre))


for i in range(1, n, 2):
    dfs(i, [i])

result = max(result, reduce([]))

print(result)
