'''
2. 재귀함수
   2)재귀함수 연습
        (4) 리스트뒤집기 : 파라미터로 리스트 some_list를 받고, 뒤집힌 리스트를 리턴해 주는 재귀 함수 flip을 쓰세요.
'''

# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    listLen = len(some_list)
    if listLen<2:
        return some_list
    else:
        return some_list[-1:] + flip(some_list[:-1])
    

#지수꺼
def flip2(some_list):
    if len(some_list)<=1:
        return some_list
    else:
        some_list=some_list[-1:]+flip(some_list[:-1])
        return some_list



# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)