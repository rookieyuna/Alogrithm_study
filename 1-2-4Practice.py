'''
1. 알고리즘의 정석
   2)하나의 문제 여러가지 알고리즘
        (4) 실습과제
            ‘이진 탐색(Binary Search)’ 알고리즘을 사용해서 어떤 원소가 리스트 안에 포함되어 있는지 확인하세요
                =>이진 탐색: 중간의 인덱스로 탐색범위를 반으로 줄여가며 진행하는 알고리즘 (정렬된 리스트를 전제로 함)
            파라미터로 탐색할 값 element와 리스트 some_list를 받는 함수 binary_search를 작성하세요. 
           
            리스트의 첫 번째 인덱스와 마지막 인덱스의 값을 합하여 2로 나눈 후, 중간 인덱스로 지정합니다. 
            그리고 그 인덱스에 해당하는 값이 element인지 확인해봅니다.
            아닌 경우 해당 인덱스 값이 element보다 큰지 작은지 비교하여  탐색범위를 제외시킵니다.
            이를 반복하여 진행하고 element가 몇번쨰 인덱스에 위치해있는지 확인하여 반환합니다.
           
'''

#힌트참조하고 푼답 ㅋㅋㅋㅋ
def binary_search(element, some_list):
    start = 0
    end = len(some_list)-1
    
    while start<=end:
        mIdx = (start+end)//2
        if some_list[mIdx] == element:
            return mIdx
        elif some_list[mIdx] > element:
            end=mIdx-1
        else:
           start=mIdx+1
    return "None"


#정답
def binary_search2(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1
    
    while start_index <= end_index:
        midpoint = (start_index + end_index) // 2
        if some_list[midpoint] == element:
            return midpoint
        elif some_list[midpoint] > element:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1
    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))


