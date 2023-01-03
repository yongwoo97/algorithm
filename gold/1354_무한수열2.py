n, p, q, x, y = map(int, input().split())
import sys
sys.setrecursionlimit(1000000000)
#dp = [0] * 1000000
di = {}
def recur(target, pp, qq, xx, yy):
    if target <= 0:
      #  dp[target] = 1
        return 1

    if target in di:
        return di[target]

    di[target] = recur(target // pp -xx, pp, qq, xx, yy) + recur(target // qq -yy, pp, qq, xx, yy)
    return di[target]

print(recur(n, p, q, x, y))
