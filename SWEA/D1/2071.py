# 2071 - 평균값 구하기
import sys
input = sys.stdin.readline

T = int(input())
for test_case in range(1, T + 1):
    test_list = list(map(int, input().split()))
    # 평균값 구하기
    average = round((sum(test_list) / 10))
    print(f"#{test_case} {average}")
