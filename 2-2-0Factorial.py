#팩토리얼 재귀함수
def Factorial(n):
    if n == 0:
        return 1
    return Factorial(n-1) * n

print(Factorial(5)) #=120

#팩토리얼 for문
def FactorialFor(n):
    total = 1
    for i in range(1,n):
        total *= (i+1)        
    return total

print(FactorialFor(5))