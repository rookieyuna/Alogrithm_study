'''
3. 알고리즘 패러다임
   2)Divide and Conquer
        (4) 1부터 n까지의 합
        Divide and Conquer를 이용해서 1부터 n까지 코드로 구현하기
        우리가 작성할 함수 consecutive_sum은 두 개의 정수 인풋 start와 end를 받고, 
        start부터 end까지의 합을 리턴합니다. end는 start보다 크다고 가정합니다.
'''

def consecutive_sum(start, end):
    # base case        
    if end == start:
        return start

    # 부분 문제를 반으로 나눠주기 위해서 문제의 정중앙을 정의한다 (Divide)
    mid = (start + end) // 2

    # 각 부분 문제를 재귀적으로 풀고(Conquer), 부분 문제의 답을 서로 더한다(Combine).
    return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)

# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))

'''
[출력결과]
55
5050
32131
75466
'''