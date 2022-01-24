'''
2. 재귀함수
   2)재귀함수 연습
        (5) 이진탐색 알고리즘 : 재귀함수로 이진탐색 알고리즘 구현하기
'''

def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1
    
    # 코드를 작성하세요.
    if start_index <= end_index:
        midpoint = (start_index + end_index) // 2
        if some_list[midpoint] == element:
            return midpoint
        elif some_list[midpoint] > element:
            return binary_search(element, some_list, start_index, midpoint - 1)
        else:
            return binary_search(element, some_list, midpoint + 1, end_index)




print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))