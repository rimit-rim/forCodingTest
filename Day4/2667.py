'''
https://www.acmicpc.net/problem/2667
2667 - 단지번호붙이기
'''
import sys
input = sys.stdin.readline

graph = []
count = 0

# 입력
N = int(input())
for _ in range(N):
    graph.append(list(map(int, input().strip())))

visited = [[False] * N for _ in range(N)]   # 방문 여부
result = [] # 단지별 집 개수 저장 리스트

# DFS(재귀방식)
def dfs(x, y):
    global count
    visited[x][y] = True
    count += 1
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                dfs(nx, ny)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            count = 0    # 새 단지 시작 → 카운트 초기화
            dfs(i, j)   # dfs 탐색 시작
            result.append(count)    # 단지 크기 저장

print(len(result))
for r in sorted(result):
    print(r)