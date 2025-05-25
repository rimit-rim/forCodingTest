# 2072_홀수만 더하기

import sys
input = sys.stdin.readline

T = int(input())
for test_case in range(1, T + 1):
    test_list = list(map(int, input().split()))

    test_sum = 0
    for i in range(10):
        if (test_list[i] % 2) == 1:
            test_sum += test_list[i]
    print(f"#{test_case} {test_sum}")