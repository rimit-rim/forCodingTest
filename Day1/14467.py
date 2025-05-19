'''
14467 - 소가 길을 건너간 이유1
존이 할 일은 소가 길을 건너는 것을 관찰하는 것이다.
존은 소의 위치를 N번 관찰하는데, 각 관찰은 소의 번호와 소의 위치 하나씩으로 이루어져 있다.
존은 소를 10마리 가지고 있으므로 소의 번호는 1 이상 10 이하의 정수고, 소의 위치는 길의 왼쪽과 오른쪽을 의미하는 0과 1 중 하나다.

이 관찰 기록을 가지고 소가 최소 몇 번 길을 건넜는지 알아보자.
즉 같은 번호의 소가 위치를 바꾼 것이 몇 번인지 세면 된다.
'''
import sys
input = sys.stdin.readline

# 관찰 횟수
N = int(input())

# 각 소의 위치 상태 기록
cow_position = dict()

# 위치가 바뀐 횟수
change_count = 0

for _ in range(N):
    cow, pos = map(int, input().split())

    # 이전에 본 적이 있는 소라면
    if cow in cow_position:
        # 위치가 바뀌었다면
        if cow_position[cow] != pos:
            change_count += 1
    # 현재 위치 기록 및 갱신
    cow_position[cow] = pos
print(change_count)