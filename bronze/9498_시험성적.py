s = int(input().rstrip())

if s >= 90:
    print('A')
elif s < 90 and s >= 80:
    print('B')
elif s < 80 and s >= 70:
    print('C')
elif s < 70 and s >= 60:
    print('D')
else:
    print('F')
