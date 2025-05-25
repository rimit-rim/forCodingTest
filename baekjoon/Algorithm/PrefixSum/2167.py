'''
2167 - 2차원 배열의 합
2차원 배열이 주어졌을 때 (i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합을 구하는 프로그램을 작성하시오.
배열의 (i, j) 위치는 i행 j열을 나타낸다.
'''
import sys
input = sys.stdin.readline

array = []
idx = []

# 입력
N, M = map(int, input().split())
for i in range(N):
    array.append(list(map(int, input().split())))
K = int(input())
for i in range(K):
    idx.append(list(map(int, input().split())))

for a in range(0, K):
    sum = 0
    # 좌표 변환
    i, j, x, y = idx[a][0]-1, idx[a][1]-1, idx[a][2]-1, idx[a][3]-1
    # 순환
    for row in range(i, x+1):
        for col in range(j, y+1):
            sum += array[row][col]
    # 출력
    print(sum)