'''
https://www.acmicpc.net/problem/10869
10869 - 사칙연산
'''
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)