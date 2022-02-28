class absheap:
    def __init__(self):
        self.q = [0]

    def show(self):
        print(self.q)

    def size(self):
        return len(self.q) - 1

    def upheap(self, i):
        while i > 1 and abs(self.q[i]) <= abs(self.q[i//2]):
            if abs(self.q[i]) == abs(self.q[i//2]) and self.q[i] < self.q[i//2]:
                self.q[i // 2], self.q[i] = self.q[i], self.q[i // 2]
                i = i // 2

            elif abs(self.q[i]) < abs(self.q[i//2]):
                self.q[i//2], self.q[i] = self.q[i], self.q[i//2]
                i = i // 2
            else:
                break
    def downheap(self, i):
        N = self.size()
        #다운힙의 조건을 잘 생각해서 코드를 짜자
        while i * 2 <= N:
            k = i * 2

            if k < N and abs(self.q[k]) >= abs(self.q[k + 1]):
                if abs(self.q[k]) > abs(self.q[k+1]):
                    k += 1
                elif self.q[k] > self.q[k+1]:
                    k += 1
            if abs(self.q[i]) < abs(self.q[k]):
                break
            else:
                if abs(self.q[i]) > abs(self.q[k]):
                    self.q[i], self.q[k] = self.q[k], self.q[i]
                elif abs(self.q[i]) == abs(self.q[k]) and self.q[i] > self.q[k]:
                    self.q[i], self.q[k] = self.q[k], self.q[i]
            i = k

    def insert(self, x):
        self.q.append(x)
        self.upheap(self.size())

    def pop(self):
        if self.size() == 0:
            return 0
        else:
            self.q[1], self.q[-1] = self.q[-1], self.q[1]
            result = self.q.pop()
            self.downheap(1)
            return result

import sys
input = sys.stdin.readline
n = int(input())
a = absheap()

for _ in range(n):
    inner = int(input())
    if inner == 0:
        print(a.pop())
        #a.show()
    else:
        a.insert(inner)
        #a.show()