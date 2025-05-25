'''
2563 - 색종이
가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다.
이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다.
이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

paper = [[0] * 100 for _ in range(100)]

# 색종이 개수 입력
n = int(input())

for _ in range(n):
    # 좌표 입력 받기
    x, y = map(int, input().split())
    # 좌표~좌표+10 값이 0이라면 1로 수정
    for i in range(10):
        for j in range(10):
            if paper[x+i][y+j] == 0:
                paper[x+i][y+j] = 1
# 값이 1인 값 세기
count = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            count += 1

# 합산
print(count)