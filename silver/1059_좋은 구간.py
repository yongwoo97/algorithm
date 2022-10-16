import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()
k = int(input())

check =False
for i in range(n-1):
    if i == 0 and data[i] > 1 and data[i] > k:
        start = 1
        end = data[i] - 1
        print((k - start + 1) * (end - k  + 1) - 1)
        check= True
        break
    elif data[i] < k and data[i+1] > k:

        start = data[i] + 1
        end = data[i+1] - 1

        if start >= end:
            print(0)
            check = True
            break
        else:
            result = (k - start + 1) * (end - k  + 1) - 1
            print(result)
            check = True
            break
if not check:
    print(0)