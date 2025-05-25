'''
https://www.acmicpc.net/problem/10828
10828 - 스택
'''

import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    command = input().strip().split()

    if command[0] == "push":
        stack.append(int(command[1]))
    elif command[0] == "pop":
        # 스택에 정수가 없다면 -1 출력
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        print(1 if not stack else 0)
    elif command[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])