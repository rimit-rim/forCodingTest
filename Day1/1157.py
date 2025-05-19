import sys
input = sys.stdin.readline

word = input().strip().upper()

# 알파벳 개수 세기
counter = dict()    # 빈 딕셔너리 생성(횟수 저장 용도)
for ch in word:     # 한 글자씩 순회
    counter[ch] = counter.get(ch, 0) + 1    # 알파벳이 이미 있으면 기존값에 +1 | 없으면 0 + 1

# 가장 많이 나온 알파벳 찾기
max_count = max(counter.values())
# 값(v)이 max_count인 키(k)만 추출해서 리스트에 담음(가장 많이 나온 알파벳들만 리스트로 추림)
max_chars = [k for k, v in counter.items() if v == max_count]

if len(max_chars) > 1:
    print("?")
else:
    print(max_chars[0])