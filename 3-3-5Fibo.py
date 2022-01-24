'''
3. 알고리즘 패러다임
   3)Dynamic Programming
        (5) 피보나치수열 : 피보나치 수열이란 첫 번째 항과 두 번째 항이 1이고, 세 번째 항부터는 바로 앞의 두 항의 합으로 정의된 수열입니다.
            예를 들어서 세 번째 항은 첫 번째 항(1)과 두 번째 항(1)을 더한 2이며, 
            네 번째 항은 두 번째 항(1)과 세 번째 항(2)을 더한 3이 될 것입니다.
            이러한 방식으로 피보나치 수열의 첫 10개 항은 1, 1, 2, 3, 5, 8, 13, 21, 34, 55입니다.
            파라미터로 1 이상의 자연수 n을 받고, n번째 피보나치 수를 리턴하는 재귀 함수 fib를 쓰세요. 반복문은 쓰면 안됩니다!
            
        =>n번째 피보나치 수를 찾아주는 함수 fib_memo을 작성해 보세요.
            fib_memo는 꼭 memoization 방식으로 구현하셔야 합니다!
'''

def fib_memo(n, cache):
    if n<3:
        return 1
    if n in cache:
        return cache[n] 
    #cache.update({n : fib(n-1)+fib(n-2)})    
    cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)
    return cache[n] 

def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}
    return fib_memo(n, fib_cache)


#해설코드
def fib_memo(n, cache):
    # base case
    if n < 3:
        return 1
        
    # 이미 n번째 피보나치를 계산했으면:
    # 저장된 값을 바로 리턴한다
    if n in cache:
        return cache[n]
    
    # 아직 n번째 피보나치 수를 계산하지 않았으면:
    # 계산을 한 후 cache에 저장
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)

    # 계산한 값을 리턴한다
    return cache[n]


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))