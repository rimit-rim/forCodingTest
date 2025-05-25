'''
https://www.acmicpc.net/problem/2566
2566 - 최댓값
<그림 1>과 같이 9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때,
이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.

예를 들어, 다음과 같이 81개의 수가 주어지면 이들 중 최댓값은 90이고, 이 값은 5행 7열에 위치한다.
'''
import sys
input = sys.stdin.readline

# 배열 생성
array = [[0] * 9 for _ in range(9)]

# 입력 받기
for i in range(9):
    array[i] = list(map(int, input().split()))

max_num = 0     # 최댓값 저장
x, y = 0, 0        # 좌표 저장

# 최댓값 찾기
for i in range(9):
    for j in range(9):
        if max_num < array[i][j]:
            max_num = array[i][j]   # 최댓값 저장
            x, y = i, j     # 좌표 저장
print(max_num)
print(x+1, y+1)