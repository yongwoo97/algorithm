import sys
input = sys.stdin.readline

n = int(input())
string = input().rstrip()

def pat_arr(a):
    arr = [0] * len(a)
    j = 0
    for i in range(1, len(a)):
        while j > 0 and a[i] != a[j]:
            j = arr[j-1]
        if a[i] == a[j]:
            j += 1
            arr[i] = j

    return arr

p = pat_arr(string)[-1]
print(len(string[:n-p]))