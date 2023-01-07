#숨바꼭질과 비슷한 문제긴 하네
#이분탐색까진 안해도 될것 같고 그냥 힙큐에 넣고 돌리자.

x, y = map(int,input().split())
distance = y - x
count = 0  # 이동 횟수
move = 1  # count별 이동 가능한 거리
move_plus = 0  # 이동한 거리의 합
while move_plus < distance :
    count += 1
    move_plus += move  # count 수에 해당하는 move를 더함
    if count % 2 == 0 :  # count가 2의 배수일 때,
        move += 1
print(count)

