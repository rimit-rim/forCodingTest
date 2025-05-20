import sys
input = sys.stdin.readline

N = int(input())    # 테스트 케이스
cow = dict()    # 위치 기록 딕셔너리
count = 0       # 이동 카운트

for _ in range(N):
    cow_number, pos = map(int, input().split())

    # 본 적 있는지 판독하는 코드드
    if cow_number in cow:
        # 이전 위치와 다르면 카운트 증가
        if cow[cow_number] != pos:
            count += 1
    # 현재 위치 업데이트
    cow[cow_number] = pos
print(count)