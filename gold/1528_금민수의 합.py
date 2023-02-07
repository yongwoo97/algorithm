n = int(input())

def func(count, pre):
    result = []
    if count == 0:
        return []
    for i in ['4', '7']:
        result.append(int(pre + i))
        result += func(count - 1, pre + i)
    return result

numbers = func(6, '')
numbers.sort()
#print(numbers)
result = {i:[] for i in range(1, 1000001)}
result[4].append(4)
result[7].append(7)
from copy import deepcopy
for i in range(1, n+1):
    if not result[i]:
        continue

    for j in numbers:
        if i + j <= n and not result[i + j]:
            result[i + j] = deepcopy(result[i])
            result[i + j].append(j)


        if i + j <= n and len(result[i]) < len(result[i+j]) -1:
            result[i+j] = deepcopy(result[i])
            result[i+j].append(j)
    #print(result[n])



if result[n]:
    result[n].sort()
    print(*result[n])
else:
    print(-1)