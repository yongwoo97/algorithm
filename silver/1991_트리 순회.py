import sys
input = sys.stdin.readline

n = int(input())
data ={}
for _ in range(n):
    a, b, c = input().split()
    data[a] = [b, c]


def pre_traverse(k, root):
    if root == '.':
        return
    print(root, end = '')
    pre_traverse(k, k[root][0])
    pre_traverse(k, k[root][1])

def middle_traverse(k, root):
    if root == '.':
        return
    middle_traverse(k, k[root][0])
    print(root, end= '')
    middle_traverse(k, k[root][1])


def last_traverse(k, root):
    if root == '.':
        return
    last_traverse(k, k[root][0])
    last_traverse(k, k[root][1])
    print(root, end = '')

pre_traverse(data, 'A')
print()
middle_traverse(data, 'A')
print()
last_traverse(data, 'A')