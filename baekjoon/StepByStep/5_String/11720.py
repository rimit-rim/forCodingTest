'''
https://www.acmicpc.net/problem/11720
11720 - 숫자의 합
'''
import sys
input = sys.stdin.readline

N = int(input())

num_line = input().strip()      # 숫자 문자열

varList = list(map(int, num_line))  # 각 글자 → 정수 리스트

print(sum(varList))