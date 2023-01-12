n = int(input())

import math
dic = {}
def func(k):
    if 0 <= k <= math.pi:
        return 1
    if k in dic:
        return dic[k]
    else:

        dic[k] = (func(k-1) + func(k-math.pi)) % 1000000000000000000
        return dic[k]

print(func(n))