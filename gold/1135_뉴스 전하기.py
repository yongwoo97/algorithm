n = int(input())
data = list(map(int, input().split()))
tree = {i:[] for i in range(n)}

for i in range(1, n):

    tree[data[i]].append(i)


def func(cur):
    global tree, data, result_max

    if not tree[cur]:
        return 1

    semi_result = []
    for i in tree[cur]:
        r = func(i)
        semi_result.append(r)
    semi_result.sort()
    semi_result.reverse()
   # print(semi_result, cur)
    result_max = 0
    for i in range(len(semi_result)):
        result_max = max(result_max, i + semi_result[i])
    return result_max + 1
#print(tree)
print(func(0)-1)