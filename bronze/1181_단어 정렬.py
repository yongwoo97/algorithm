n = int(input())
li = list(set([input() for _ in range(n)]))

di = {i : [] for i in range(1, 51)}

for k in li:
    di[len(k)].append(k)


def sorting(a):
    long = len(a)
    for i in range(long-1):
        min = i
        for j in range(i+1, long):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a


for i, j in di.items():
    j = sorting(j)
    for e in j:
        print(e)



