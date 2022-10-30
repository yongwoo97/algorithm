import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input().rstrip())
k = int(input())
a = [1] * 10
if k > 0:
    data = list(map(int, input().split()))


    for i in data:
        a[i] =0
    #고장난 버튼들은 0 처리

nn = str(n)

minn = float('inf')
result = '5000000'
#print(int(''))
def dfs(s):
    global nn, a, minn, result

    if len(nn) + 1 < len(s):
        return

    if len(nn) + 1 >= len(s) >= len(nn)-1:
        if len(s) > 0 and minn > len(s) + abs(int(s)-n):
            minn = len(s) + abs(int(s)-n)
            result = s
            #print(result, minn)
            if len(nn) + 1 == len(s):
                return


    for i in range(10):
        if a[i] == 1:
            dfs(s + str(i))

dfs('')

result = len(result) + abs(int(result) - n)

#만약 버튼 + 숫자 조합보다 버튼이 더 가까울경우
if sum(a) == 0:
    print(abs(n-100))
elif result > abs(n-100):
    print(abs(n-100))
else:
    print(result)




