import sys

l = [0] * 10000
n = int(sys.stdin.readline())


for _ in range(n):
    inp = int(sys.stdin.readline())
    l[inp-1] += 1

for i in range(10000):
    if l[i] == 0:
        continue
    for _ in range(l[i]):
        print(i+1)
#왜 pypy에선 메모리 초과가 날까.

