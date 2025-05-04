t = int(input())
a = []
b = []

for i in range(0, t):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

for i in range(0, t):
    print(a[i] + b[i])
