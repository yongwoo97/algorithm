line = input().rstrip()
if len(line) > 1:
    if line[0] > line[1]:
        line = line[1] + line[0] + line[2:]
for i in range(1, len(line) - 1):
    if line[i] > line[i + 1]:
        if line[0] >= line[i+1]:
            line = line[:i+1][::-1] + line[i+1:]
            line = line[:i+2][::-1] + line[i+2:]

print(line)