n = int(input())
start = 0
data = [1]
from bisect import bisect_left, bisect_right
while data[-1] <= 1000000:
    if 4 * (start + 1) + 1 + data[start] > 1000000:
        break
    data.append(4 * (start + 1) + 1 + data[start])
    start += 1
#print(len(data))
#print(data)

result = 7
cut = 5
def recur(cur, idx, count):
    global data, result, cut
    #print(cur)
    if count >= cut:

        result = min(count, result)
        return

    if cur == n:
        #print(cur)
        result = min(count, result)
        if count == 1 or count == 2:
            print(result)
            exit()

        return

    for i in range(idx, -1, -1):
        #print(data[i], idx, count)
        if data[i] * (6 - count) < n -cur:
            break
        if cur + data[i] <= n and count < cut:
            ii = bisect_left(data, n - cur - data[i])
            recur(cur + data[i], ii, count + 1)
#print(data)
if n <= 1791:

    recur(0, 706, 0)
    print(result)

elif n <= 146858:
    cut = 4
    recur(0, 706, 0)
    print(result)
else:
    cut = 3
    recur(0, 706, 0)
    print(result)