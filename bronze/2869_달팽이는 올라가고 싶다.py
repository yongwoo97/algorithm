import math #math 모듈을 먼저 import해야 한다.

a, b, v = map(int, input().split())


net = a - b

print(int((v - b - 1) / (a - b) + 1))
