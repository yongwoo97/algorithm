n = int(input())
data = []
for _ in range(n):
    data.append(input().rstrip())
s = []
while True:
    line = input().strip()
    if not line:
        break
    line = float(line)
    s.append(line)
s.sort()
data = [113.08, 113.08 + 71.04, 113.08 + 71.04 + 87.03, 113.08 + 71.04 + 87.03 + 186.08, 113.08 + 71.04 + 87.03 + 186.08 + 131.04, round(113.08 + 71.04 + 87.03 + 186.08 + 131.04 + 128.06, 2), round(113.08 + 71.04 + 87.03 + 186.08 + 131.04 + 128.06 + 87.03, 2)]
print(data)
print(s)

dic = {}
for i in range(len(s)):
    for j in range(len(data)):
        if s[i] > data[j]:
            r = round(s[i] - data[j], 5)
            if r in dic:
                dic[r] += 1
            else:
                dic[r] = 1
print(dic)