#n2 조합으로 푸는것이 제일 빠를까?
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

min_dist = float('inf')
data.sort()
i = 0
j = n - 1
result = []
while i < j:
    tot = (data[i] + data[j])
    if abs(tot) < min_dist:
        min_dist = abs(tot)
        result = [data[i], data[j]]

    if tot > 0:
        j -= 1
    elif tot == 0:
        result = [data[i], data[j]]
        break
    else:
        i += 1

print(*result)

#비슷하게 접근했는데, 연산이 끝나서 i += 1, i -= 1을 같이하는게 아니라 결과값에
#따라서 왼쪽으로 1칸갈지 오른쪽으로 1칸 이동할지 결정해주어야 한다.
