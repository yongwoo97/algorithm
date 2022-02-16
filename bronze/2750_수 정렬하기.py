
n = int(input())
l = [int(input()) for _ in range(n)]

l = mergesort(l)
for k in l:
    print(k)