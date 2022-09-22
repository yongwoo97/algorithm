import sys
input = sys.stdin.readline

n = int(input())
residue = 1000 - n

data = [500, 100, 50, 10 , 5, 1]
count = 0
for i in range(6):
    count += (residue) // data[i]
    residue -= ((residue // data[i]) * data[i])
print(count)