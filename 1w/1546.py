import sys

t = int(input())
data = list(map(int, sys.stdin.readline().split()))
M = max(data)

tmp = 0
for i in range(t):
    tmp += (data[i] / M) * 100
print(tmp / t)