a, b, c = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

counter = 0
container = 0

def recur(a, con, m):
    if not a:
        return []
    
    for i in range(len(a)):
        if a[i] <= m and sum(con) + a[i] <= m:
            con.append(a[i])
        else:
            semi = recur(a[i+1:], con, m)
    return semi + con





for i in range(len(data)):
    container += data[i]
    remember = []
    for j in range(i, len(data)):
        if container + data[j] <= c:
            container += data[j]
            remember.append(data[j])
