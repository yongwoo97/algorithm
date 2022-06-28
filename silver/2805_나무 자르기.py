n, k = map(int, input().split())
data = list(map(int, input().split()))


mmax = max(data)
mmin = 1

while mmin <= mmax:
    mid = (mmax + mmin) // 2
    semi = 0
    for i in data:
        if i <= mid:
            continue
        else:
            semi += i - mid
    if semi >= k:
        mmin = mid + 1
    else:
        mmax = mid - 1


print(mmin-1)