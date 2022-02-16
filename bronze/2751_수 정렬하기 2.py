

#내장함수 안쓰고 정렬 하는방법 여러개가 있겠지
#삽입정렬, 선택정렬,
#머지소트로 한번 구현해봐야겠다. 병합정렬

def mergesort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2


    left = mergesort(a[:mid])
    right = mergesort(a[mid:])

    final = merge(left, right)
    return final

def merge(list1, list2):
    semi_result = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] <= list2[0]:
            semi_result.append(list1.pop(0))
        else:
            semi_result.append(list2.pop(0))

    if len(list1) >= 1:
        semi_result += list1
    if len(list2) >= 1:
        semi_result += list2

    return semi_result

n = int(input())
l = [int(input()) for _ in range(n)]

l = mergesort(l)
for k in l:
    print(k)