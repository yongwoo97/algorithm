import sys
input = sys.stdin.readline



n, k = map(int, input().split())
data = list(map(int, input().split()))
robot = [0] * (2 * n)
sid = 0
eid = n-1

cycle = 0
def turn():
    global data, robot, n
    temp = [data[-1]]
    data = temp + data[:-1]
    temp = [robot[-1]]
    robot = temp + robot[:-1]

def counter():
    global data
    count = 0
    for i in data:
        if i == 0:
            count += 1
    return count

while True:
    cycle += 1
    turn()
    if robot[eid] == 1:
        robot[eid] = 0
    for i in range(n-1, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and data[i+1] > 0:
            robot[i] = 0
            robot[i + 1] = 1
            data[i+1] -= 1
    if robot[eid] == 1:
        robot[eid] = 0
    if data[sid] > 0 and robot[sid] == 0:
        data[sid] -= 1
        robot[sid] = 1

    if counter() >= k:
        print(cycle)
        break