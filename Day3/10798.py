'''
https://www.acmicpc.net/problem/10798
10798 - 세로 읽기
'''
import sys
input = sys.stdin.readline

# 배열 선언
word = []
# 입력
for _ in range(5):
    word.append(list(input().strip()))

'''
개선된 입력
word = [list(input().strip()) for _ in range(5)]
'''

# 출력
for i in range(15):  # 열
    for j in range(5):  # 행
        if i < len(word[j]):    # 해당 자리에 요소가 존재하면
            print(word[j][i], end='')