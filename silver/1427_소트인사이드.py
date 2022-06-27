a = input()
result = []
for i in a:
    result.append(int(i))

result.sort()
result = result[::-1]
result = list(map(str, result))
print(''.join(result))