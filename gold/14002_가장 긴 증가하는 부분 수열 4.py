import sys
n = int(input())
data = list(map(int, input().split()))

arr = [0] * n
arr1 = []
real_max = 0
max_idx = 0
for i in range(n):
    maxx = arr[i]
    temp = [data[i]]
    k=[]

    #nlogn 수준으로 찾으려면
    #여기서 이분 탐색을 적용해야하네
    #근데 어떻게 적용 할 수 가 있지?
    
    for j in range(i-1, -1, -1):
        if data[i] > data[j]:
            temp1 = maxx
            maxx = max(maxx, arr[j])
            if temp1 != maxx:
                k = arr1[j] + temp

    if maxx == 0:
        arr[i] = 1
        arr1.append(temp)
    else:
        arr[i] = maxx + 1
        arr1.append(k)
    semi = real_max
    real_max = max(arr[i], real_max)
    if semi != real_max:
        max_idx = i


print(arr[max_idx])
print(*arr1[max_idx])