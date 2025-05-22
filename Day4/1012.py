'''
https://www.acmicpc.net/problem/1012
1012 - 유기농 배추
'''
import sys
input = sys.stdin.readline

# 입력
T = int(input())    # 테스트 케이스 수

for _ in range(T):
    row, col, veg = map(int, input().split())   # 가로, 세로, 배추
    graph = [[0] * row for _ in range(col)]     # 기본 그래프 생성
    for _ in range(veg):
        x, y = map(int, input().split())
        graph[y][x] = True

    visited = [[0] * row for _ in range(col)]   # 방문여부

    # dfs
    def dfs(x, y):
        global count
        visited[y][x] = 1 # 현재 좌표 방문 체크

        # 상하좌우 이동
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy

            # 1. 배열 범위 안에 있고
            if 0 <= nx < row and 0 <= ny < col:
                # 2. 배추가 있고, 아직 방문하지 않았다면
                if graph[ny][nx] == 1 and visited[ny][nx] == 0:
                    dfs(nx, ny)

    count = 0
    for y in range(col):
        for x in range(row):
            if graph[y][x] == 1 and visited[y][x] == 0:
                dfs(x, y)
                count += 1

    print(count)