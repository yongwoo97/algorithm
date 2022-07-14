#일단 힙 자료구조를 한번 구현해보자
from collections import deque
'''
class heap:
    def __init__(self):
        self.arr = deque()


    def put(self, x):
        if len(self.arr) == 0:
            self.arr.append(x)
            print('put complete')
            return
        else:
            self.arr.appendleft(x)
            index = 1
            while True:

                if len(self.arr) > (index * 2):
                    if self.arr[index * 2 - 1] > self.arr[index * 2]:
                        next = index * 2
                    else:
                        next = index * 2 + 1
                elif len(self.arr) == index:
                    break
                elif len(self.arr) == (index * 2):
                    next = index * 2

                print(index, next)
                if self.arr[next-1] > self.arr[index-1]:
                    self.arr[index-1], self.arr[next-1] = self.arr[next-1], self.arr[index-1]
                else:
                    break

                index = next

    def pop(self):
        m = self.arr[0]
        del self.arr[0]
        if len(self.arr) >= 2:
            if self.arr[0] < self.arr[1]:
                self.arr[0], self.arr[1] = self.arr[1], self.arr[0]
        return m

    def get(self):
        return self.arr

a = heap()
a.put(4)
a.put(3)
a.put(5)
a.put(1)
print(a.get())

a.pop()
print(a.get())
'''
import sys, heapq

input = sys.stdin.readline
heap = []

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    if not heap:
        for a in arr:
            heapq.heappush(heap, a)
    else:
        for a in arr:
            if heap[0] < a:
                heapq.heappush(heap, a)
                heapq.heappop(heap)

print(heap[0])