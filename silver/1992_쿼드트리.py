import sys

input = sys.stdin.readline
n = int(input())
data = []
for _ in range(n):
    line = list(map(int, list(input().rstrip())))
    data.append(line)

def divide(k):
    if len(k) == 1:
        print(str(k[0][0]))
    if len(k) < 2:
        return ''


    dir = [(0, 0), (0, 1), (1, 0), (1, 1)]
    if len(k) == 2:
        s = '('
        standard = k[0][0]
        count = False
        for i, j in dir:
            s += str(k[i][j])
            if standard != k[i][j]:
                count = True

        if not count:
            return s[1]
        else:
            return s + ')'



    mid = len(k) // 2
    s = ''
    for i in dir:
        nx = i[0] * mid
        ny = i[1] * mid

        semi_result = divide([i[ny:ny+mid] for i in k[nx:nx+mid]])


        s += semi_result


    st = s[0]
    check = True
    for i in s:
        if i != st:
            check = False

    if check:
        return st


    return '(' + s + ')'

print(divide(data))