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
   # print(arr)
   # print()
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

from copy import deepcopy
result = 0
def dfs(start):
    global result
    if start >= n-4:
        data_copy = deepcopy(data1)
        idx = data1[start]

        if idx == '+':
            mid = data_copy[start - 1] + data_copy[start + 1]
            data_copy = data_copy[:start - 1] + [mid] + data_copy[start + 2:]

        elif idx == '-':
            mid = data_copy[start - 1] - data_copy[start + 1]
            data_copy = data_copy[:start - 1] + [mid] + data_copy[start + 2:]

        else:
            mid = data_copy[start - 1] * data_copy[start + 1]
            data_copy = data_copy[:start - 1] + [mid] + data_copy[start + 2:]
        result = max(result, cal(data_copy))
        return [start]



    for i in range(start + 4, n, 2):
        q = [start]
      #  print(i)
      #  print(dfs(i))
        q += dfs(i)
      #  print(q)
        data_copy = deepcopy(data1)
        count = 0
        for j in range(len(q)):
            idx = data1[q[j]]

            if idx == '+':
                mid = data1[q[j]-1] + data1[q[j] + 1]
                data_copy = data_copy[:q[j] + (count * -1 * 2) -1] + [mid] + data_copy[q[j] + (count * -2) +2:]

            elif idx == '-':
                mid = data1[q[j] - 1] - data1[q[j] + 1]
                data_copy = data_copy[:q[j] + (count * -2) - 1] + [mid] + data_copy[q[j] + (count * -2) + 2:]

            else:
                mid = data1[q[j] - 1] * data1[q[j] + 1]
                data_copy = data_copy[:q[j] + (count * -2) - 1] + [mid] + data_copy[q[j] + (count * -2) + 2:]
            count += 1
      #  print(q)
        result = max(result, cal(data_copy))
    return [start]
for i in range(1, n, 2):
    dfs(i)
  #  print()
result = max(result, cal(data1))

print(result)