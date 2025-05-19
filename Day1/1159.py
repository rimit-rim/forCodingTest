import sys
input = sys.stdin.readline

n = int(input())     # 횟수 입력
counter = dict()

for _ in range(n):    # 반복 입력 받음
    name = input().strip()
    first_letter = name[0]
    # 등장 횟수
    counter[first_letter] = counter.get(first_letter, 0) + 1

# 5명 이상인 알파벳만 뽑아서 정렬
result = []
for k, v in counter.items():
    if v >= 5:
        result.append(k)
result.sort()

if result:
    print("".join(result))
else:
    print("PREDAJA")




