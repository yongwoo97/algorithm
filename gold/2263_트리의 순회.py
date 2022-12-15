
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
import sys
sys.setrecursionlimit(1000000)
idx = [0] * (n+1)
for i in range(n):
    idx[inorder[i]] = i

#print(idx)
def find(s1, e1, s2, e2):

    if s1 > e1 or s2 > e2:
        return

    #print(postorder[e2], end=' ')

    mid = idx[postorder[e2]]

    left_len = mid - s1
    print(mid, left_len)
    #print(mid, postorder[e2], left_len)
    find(s1, mid-1, s2, left_len-1)
    find(mid + 1, e1, left_len, e2 - 1)


find(0, n-1, 0, n-1)



