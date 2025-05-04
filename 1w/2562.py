data = []

for i in range(9):
    x = int(input())
    data.append(x)

print(max(data))
print(data.index(max(data)) + 1)
