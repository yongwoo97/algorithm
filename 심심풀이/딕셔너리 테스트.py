from bisect import bisect_left, bisect_right

a = [4, 9]
x = 4

print(bisect_left(a, x)) # 2
print(bisect_right(a, x)) # 6
#print(bisect_right(a, x) - bisect_left(a, x)) # 4


def bina(a, n):
    low = 0
    high = len(a) - 1

    while low < high:
        mid = (low + high) // 2
        if n >= a[mid]:
            low = mid + 1
        else:
            high = mid-1

    return low

print(bina(a, x))