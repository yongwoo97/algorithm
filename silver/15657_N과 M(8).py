n, m = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

def permute(d, k, cur):
    if k == 0:
        print(*cur)
        return

    for i in range(n):
        pivot = d[i]
        if cur and cur[-1] <= pivot:
            permute(d, k-1, cur + [pivot])
        elif not cur:
            permute(d, k-1, cur + [pivot])


permute(data, m, [])


