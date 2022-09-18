
def binary(lis_arr, num):

    low = -1
    high = len(lis_arr)

    while low + 1 < high:
        mid = (low + high) // 2

        if num > lis_arr[mid]:
            low = mid

        else:
            high = mid


    return high

import sys
input = sys.stdin.readline

a = [1,2]
print(binary(a, 1))

n = int(input())
data = list(map(int, input().split()))
memo = [0] * n
temp = [-1000000001]

for i in range(n):
    if data[i] > temp[-1]:
        temp.append(data[i])
        memo[i] = len(temp) - 1
    else:
        memo[i] = binary(temp, data[i])
        temp[memo[i]] = data[i]



mmax = max(memo)
result = []
for i in range(n-1, -1, -1):
    if memo[i] == mmax:
        result.append(data[i])
        mmax -= 1

print(len(result))
result.reverse()
print(*result)
