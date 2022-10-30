#재귀함수 + dp(딕셔너리 활용)
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
dic = {0:1}

def func(k):

    if k in dic:
        return
    dic[k] = 0
    func(k//b)
    func(k//c)
func(a)
a1 = sorted(dic)


for i in a1:
    if i == 0:
        continue
    dic[i] = dic[i//b] + dic[i//c]

print(dic[a])
