import sys

input = sys.stdin.readline
n = int(input())
data1 = list(input().rstrip())
for i in range(0, n, 2):
    data1[i] = int(data1[i])



def dfs(data):

    if len(data) == 1:
        return data[0]
    result = 0
    for i in range(1, len(data), 2):

        if data[i] == '+':
            temp = data[i-1] + data[i+1]
        elif data[i] == '-':
            temp = data[i-1] - data[i+1]
        else:
            temp = data[i-1] * data[i+1]

        if i + 2 < len(data):
            if data[i+2] == '+':
                semi = temp + dfs(data[i+3:])
            elif data[i+2] == '-':
                semi = temp - dfs(data[i+3:])
            else:
                semi = temp * dfs(data[i+3:])
            result = max(semi, result)
        result = max(temp, result)
    return result


re = 0
for i in range(1, len(data1), 2):
    if i == 1:
        pre = dfs(data1)
        re = max(re, pre)
        print(re, '1235dsf')
        continue
    pre = data1[0]
    for j in range(3, i-2, 2):
        if data1[j] == '+':
            pre += data1[j+1]
        elif data1[j] == '-':
            pre -= data1[j+1]
        else:
            pre *= data1[j+1]
    if  i - 2 > 0:
        if data1[i-2] == '+':
            s = pre + dfs(data1[i-1:])
        elif data1[i-2] == '-':
            s = pre - dfs(data1[i-1:])
        else:
            s = pre * dfs(data1[i-1:])
        re = max(re, s)
    print(re)
    re = max(pre, re)
print(dfs(data1))