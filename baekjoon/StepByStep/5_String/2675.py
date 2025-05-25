'''
2675 - 문자열 반복
문자열 S를 입력받은 후에, 각 문자를 R번 반복해
새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.
S에는 QR Code "alphanumeric" 문자만 들어있다.

QR Code "alphanumeric" 문자는
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
'''
import sys
input = sys.stdin.readline

# 입력 받기
T = int(input())    # 테스트케이스 개수

# 테스트케이스 반복
for _ in range(T):
    r, s = input().split()  # 반복횟수(r), 문자열(s) 입력받기
    r = int(r)              # r 형변환
    for ch in s.strip():        # 문자열 한 글자씩 반복
        print(ch * r, end="")   # 각 문자를 r번 반복해서 출력
    print()     # 줄바꿈
