i = input()

idx = 0
l = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0
while idx < len(i):
    if i[idx:idx+3] == 'dz=':
        idx += 3
        count += 1
    elif i[idx:idx+2] in l:
        idx += 2
        count += 1
    else:
        idx += 1
        count += 1

print(count)
