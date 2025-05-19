import sys
input = sys.stdin.readline

al = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input().strip()

for c in al:
    word = word.replace(c, "*") # 크로아티아 알파벳은 * 하나로 대체
print(len(word))