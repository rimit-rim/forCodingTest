# 1859 백만장자 프로젝트
import sys
input = sys.stdin.readline

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))

    max_price = 0
    profit = 0

    for price in reversed(prices):
        if price > max_price:
            max_price = price
        else:
            profit += max_price - price

    print(f"#{test_case} {profit}")