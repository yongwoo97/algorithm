class myheap:
    def __init__(self):
        self.pq = [0]
        self.makeq()

    def show(self):
        return self.pq

    def makeq(self):
        for i in range(self.size()//2, 0, -1):
            self.downheap(i)

    def size(self):
        return len(self.pq)-1

    def downheap(self, i):
        while 2 * i <= self.size():
            k = 2 * i
            if k < self.size() and self.pq[k] > self.pq[k+1]:
                k += 1
            if self.pq[i] < self.pq[k]:
                break
            self.pq[k], self.pq[i] = self.pq[i], self.pq[k]
            i = k

    def upheap(self, i):
        while i > 1 and self.pq[i//2] > self.pq[i]:
            self.pq[i], self.pq[i//2] = self.pq[i//2], self.pq[i]
            i = i // 2

    def outer(self):
        if self.size() == 0:
            return 0
        else:
            self.pq[1], self.pq[-1] = self.pq[-1], self.pq[1]
            result = self.pq.pop(-1)
            self.downheap(1)
            return result

    def insert(self, x):
        self.pq.append(x)
        self.upheap(self.size())

import sys
input = sys.stdin.readline
a = myheap()
n = int(input())
for _ in range(n):
    inner = int(input())
    if inner == 0:
        print(a.outer())
    else:
        a.insert(inner)

