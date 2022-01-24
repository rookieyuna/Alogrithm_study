'''
1. 알고리즘의 정석
    1)알고리즘이란?
        (5) 실습과제
            팔린드롬(palindrome) : 거꾸로 읽어도 똑같은 단어
            인자로 전달되는 'word'가 팔린드롬이면 True를, 팔린드롬이 아니면 False를 리턴하는
            is_palindrome 함수를 만드세요      
'''

def is_palindrome(word):
    for i in range((len(word)//2)+1):
        if word[i]!=word[-(i+1)]:
            return False
    else:
        return True

#지수코드
def is_palindrome_js(word):
    length = len(word)
    for i in range(0, length):
        if word[i]==word[-(i+1)]:
            continue
        return False
    else:
        return True

#모르는사람꺼
def is_palindrome_st(word):
    list_word = list(word)
    reversed_word = ''.join(reversed(list_word))
    return reversed_word == word


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
