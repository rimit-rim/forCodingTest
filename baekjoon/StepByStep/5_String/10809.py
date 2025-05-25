'''
10809 - 알파벳 찾기
알파벳 소문자로만 이루어진 단어 S가 주어진다.
각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

# 입력 받기
s = input().strip()

# 알파벳 리스트 만들기
alphabets = 'abcdefghijklmnopqrstuvwxyz'

# 알파벳마다(a to z) 한번씩 반복
for ch in alphabets:
    # 현재 알파벳이 word에 처음 등장 하는 위치 출력(없으면 -1)
    print(s.find(ch), end=" ")