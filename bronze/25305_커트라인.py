import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
data = data[::-1]
print(data[k-1])