'''
1. 알고리즘의 정석
   2)하나의 문제 여러가지 알고리즘
        (3) 실습과제
            '선형 탐색(Linear Search)' 알고리즘을 사용해서 어떤 원소가 리스트 안에 포함되어 있는지 확인하세요
                =>선형 탐색: 리스트의 처음부터 끝까지 순서대로 하나씩 탐색을 진행하는 알고리즘 
            파라미터로 탐색할 값 element와 리스트 some_list를 받는 함수 linear_search를 작성하세요. 
            0번 인덱스부터 순서대로 하나씩 확인해서 만약 element를 some_list에서 발견할 시 그 위치(인덱스)를 리턴해 주면 됩니다.
            element가 some_list에 존재하지 않는 값이면 None을 리턴해주세요.
            ※element in some_list 는 사용하면 안됩니다. 반드시 반복문을 사용해서 해결해 주셔야 합니다.  
'''

def linear_search(element, some_list):
    for i in range(len(some_list)):
        if some_list[i] == element:
            return i
    else:
        return None

#지수코드
def linear_search_js(element, some_list): 
    j = -1
    for i in some_list:
        j += 1
        if element == i:
            return j


print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))