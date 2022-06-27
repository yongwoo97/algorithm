import sys
sys.setrecursionlimit(100000000)

n, k = map(int, input().split())
'''
memo = [1]
for i in range(2, n+1):
    memo.append(memo[-1] * i)

result = int(memo[n-1] / (memo[k-1] * memo[n-k-1]))
print(result)

#위에 코드는 가장 간단하게 구현한 것인데 메모리초과가 뜬다. 4백만이니 그럴 수 밖에 없지. 그렇다면 어떻게?
#
'''

def func(a, b):
    if a == b or b == 0:
        return 1


    temp = func(a-1, b-1) + func(a-1, b)

    return temp % 1000000007

print(func(n, k))