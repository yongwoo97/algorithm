ans = 0

def back(cur, visited, s, cnt):
    global ans
    if len(s) == cnt:
        ans += 1
        return

    for i in range(26):
        if visited[i] > 0 and cur[cnt-1] != chr(97 + i):
            visited[i] -= 1
            back(cur + chr(97+i), visited, s, cnt + 1)
            visited[i] += 1


s = input().rstrip()

cur = ""
visited = [0] * 26
for i in s:
    visited[ord(i)-97] += 1

for i in range(26):
    if visited[i] > 0:
        visited[i] -= 1
        back(cur+chr(97+i), visited, s, 1)
        visited[i] += 1
print(ans)