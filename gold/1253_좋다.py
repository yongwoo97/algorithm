import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))

data.sort()
count = 0
#print(data)
for i in range(n):

    start = 0
    end = n-1
    #print(i)
    while start < end:
        if end == i:
            end -= 1
            continue
        if start == i:
            start += 1
            continue
        if data[start] + data[end] == data[i]:
            count += 1
            break
        elif data[start] + data[end] > data[i]:
            end -= 1
        else:
            start += 1
print(count)
