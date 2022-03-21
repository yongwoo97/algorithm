n = input()
if len(n) < 2:
    n = '0' + n

n1 = n
count = 0
while n[1] + str(int(n[0]) + int(n[1]))[-1] != n1:
    #print(n)
    nn = str(int(n[0]) + int(n[1]))
    n = n[1] + nn[-1]
    count += 1
    #print(n)
count += 1
print(count)