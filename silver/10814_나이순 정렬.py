'''
n = int(input())
member_lst = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    member_lst.append((age, name))

member_lst.sort(key = lambda x : x[0])	## (age, name)에서 age만 비교

for i in member_lst:
    print(i[0], i[1])



# 퀵소트 구현

def quick(a, b):
    global arr
    if a >= b:
        return
    i = a
    j = b
    mid = (a + b) // 2

    while i < j:
        print(i, j)
        while arr[i] <= arr[mid] and i < b:
            i += 1
        while arr[j] >= arr[mid] and j > a:
            j -= 1
        print(i, j, 'hello')
        if j <= i:
            print(mid)
            arr[mid], arr[j] = arr[j], arr[mid]
            mid = j
            print(mid)
            break
        arr[i], arr[j] = arr[j], arr[i]

    quick(a, mid - 1)
    quick(mid + 1, b)

quick(0, len(arr)-1)
print(arr)

'''
#퀵정렬 배열버전

def quick(data):
   # print(data)
    if len(data) < 2:
        return data
    i = 0
    j = len(data) - 1

    mid = (i + j) // 2
    print(data)
    while i <= j:
        #print(i, j)
        while data[i] < data[mid] and i < len(data)-1:
            i += 1
        while data[j] > data[mid] and j > 0:
            j -= 1
        #print(i, j, 'hello')
        if j < i:
            #print(mid)
            data[mid], data[j] = data[j], data[mid]
            mid = j
            #print(mid)
        else:
            data[i], data[j] = data[j], data[i]
    print(data)
    return quick(data[0:mid]) + [data[mid]] + quick(data[mid+1:])

arr = [10, 3, 4, 5, 6]
print(quick(arr))


def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = (start+end) // 2 # 피벗은 첫 번째 원소
    left = start
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        #print(array)
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
       # print(array)
    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(arr, 0, len(arr)-1)
print(arr)