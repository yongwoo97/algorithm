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
    print(data)
    if len(data) < 2:
        return data
    i = 0
    j = len(data) - 1

    mid = (i + j) // 2

    while i < j:
        print(i, j)
        while data[i] <= data[mid] and i < len(data)-1:
            i += 1
        while data[j] > data[mid] and j > 0:
            j -= 1
        print(i, j, 'hello')
        if j <= i:
            print(mid)
            data[mid], data[j] = data[j], data[mid]
            mid = j
            print(mid)
            break
        data[i], data[j] = data[j], data[i]

    return quick(data[0:mid]) + [data[mid]] + quick(data[mid+1:])
arr = [5, 3, 2, 2, 100, 7]
print(quick(arr))
