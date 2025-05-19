'''
10988 - 팰린드롬인지 확인하기
알파벳 소문자로만 이루어진 단어가 주어진다.
이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.
'''
import sys

# 입력받기
input = sys.stdin.readline
word = input().strip()

# 뒤집은 문자열 만들기
reversed_word = word[::-1]

# 조건에 따라 출력
if word == reversed_word:
    print("1")
else:
    print("0")
