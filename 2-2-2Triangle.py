'''
2. 재귀함수
   2)재귀함수 연습
        (2) 숫자합 : n번째 삼각수(triangle number)는 자연수 1부터 n까지의 합입니다. 
        파라미터로 정수값 n을 받고 n번째 삼각수를 리턴해주는 재귀 함수 triangle_number를 쓰세요. 
'''

# 1부터 n까지의 합을 리턴
def triangle_number(n):
    if n ==1 : 
        return 1
    else:
        return triangle_number(n-1)+n

#다른분 새로운 방법 (재귀는아니지만,,)
def sum_generator(N):
    return sum(n for n in range(1, N+1))


# 테스트: triangle_number(1)부터 triangle_number(10)까지 출력
for i in range(1, 11):
    print(triangle_number(i))

'''
[출력결과]
1
3
6
10
15
21
28
36
45
55
'''

