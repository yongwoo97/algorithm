N = int(input())
nlist = list(map(int, input().split()))
M = int(input())
mlist = list(map(int, input().split()))

di = {}
for i in nlist:
    if i in di:
        di[i] += 1
    else:
        di[i] = 1

for k in mlist:
    if k in di:
        print(di[k], end = ' ')
    else:
        print(0, end = ' ')

