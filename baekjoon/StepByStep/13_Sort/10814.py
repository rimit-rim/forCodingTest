'''
https://www.acmicpc.net/problem/10814
10814 - 나이순 정렬
'''
import sys
input = sys.stdin.readline

own = []

T = int(input()) #테스트케이스
for _ in range(T):
    age, name = input().split()
    own.append((int(age), name))

# 정렬
own.sort(key=lambda x: x[0])

for age, name in own:
    print(age, name)