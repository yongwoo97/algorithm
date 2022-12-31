#이제 세그먼트 트리에 대해서 배워보자
#구간합을 빠르게 구하는 방법 O(logN) 수준으로
#일단 세그먼트 트리부터 구현해야지
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())

data = [] #
for _ in range(n):
    line = int(input())
    data.append(line)

tree = [0] * (n * 4) #충분한 트리의 공간을 선언해주고
print(data)
#이제 아래는 구간합 트리를 초기화 해주는 함수. 재귀로 구현한다.
#일단 아래 함수가 맞나 체크를 좀 해봐야겠지?

def initiate(left, right, node):
    global tree

    #기저 조건
    if left == right:
        tree[node] = data[left]
        return tree[node]

    mid = (left + right) // 2
    tree[node] = initiate(left, mid, node * 2) + initiate(mid + 1, right, node * 2 + 1)

    return tree[node]


initiate(0, n-1, 1)
#트리는 완성되었다. 이제 구간합을 구하는 함수를 만들어보자.
#기본개념은 range에 해당하는 노드들을 다 더하면 된다.
#이또한 재귀적으로 구현해야 한다.

def sumquery(start, end, left, right, node):
    #일단 범위를 벗어 났을때는 취소해줘야지
    if end < left or start > right:
        return 0

    if left <= start and end <= right:
      #  print(tree[node])
        return tree[node]

    mid = (start + end ) // 2
    result = sumquery(start, mid, left, right, node * 2) + sumquery(mid + 1, end, left, right, node * 2 + 1)
    return result


def update(start, end, node, idx, value):
    if idx < start or end < idx:
        return
    tree[node] = value

    if start == end:
        return

    mid = (start + end) // 2
    update(start, mid, node * 2, idx, value)
    update(mid + 1, end, node * 2 + 1, idx, value)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, n-1, 1, b, c)
    else:
        print(sumquery(0, n-1, b, c, 1))
    print(tree)