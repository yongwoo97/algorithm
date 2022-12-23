#중복 허용 안함, 순열은 오름차순으로 출력해야함
#음... 중복허용 어떻게 해결할꺼야?
#방문배열로 한번해보자
n, m = map(int, input().split())
data = list(map(int, input().split()))
s = set()
def func(cur, idx, k):
   # global visited
    if k == 0:
        s.add(cur)
        return

    for i in range(idx, n):
       # if visited[data[i]] == 0:
        if cur and cur[-1] <= data[i]:
    #        visited[data[i]] = 1
            func(cur + (data[i], ), i, k-1)
        else:
            break



data.sort()
for i in range(n):
    func((data[i], ), i, m-1)

s = list(s)
s.sort()
for i in s:
    print(*i)

