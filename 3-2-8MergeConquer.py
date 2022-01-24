'''
3. 알고리즘 패러다임
   2)Divide and Conquer
        (8) 합병정렬 함수작성
        Divide and Conquer 방식으로 merge_sort 함수를 작성해보세요
        merge_sort는 파라미터로 리스트 하나를 받고, 정렬된 새로운 리스트를 리턴합니다.
'''

def merge(list1, list2):
    i, j = 0, 0
    new_list = []
    
    while i<len(list1) and j<len(list2):
        if list1[i]<list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1
        
    if i==len(list1):
        new_list += list2[j:]
    elif j==len(list2):
        new_list += list1[i:]
    
    return new_list
    
    
# 합병 정렬
def merge_sort(my_list):
    
    if len(my_list)<2:
        return my_list
    
    mid = len(my_list)//2
    listA = my_list[:mid]
    listB = my_list[mid:]

    return merge(merge_sort(listA),merge_sort(listB))


#지수답
def merge_sort2(my_list):
    if len(my_list) < 2:
        return my_list
    mididx = len(my_list)//2

    return merge(merge_sort(my_list[mididx:]), merge_sort(my_list[:mididx]))


#해설답
def merge_sort3(my_list):
    # base case
    if len(my_list) < 2:
        return my_list

    # my_list를 반씩 나눈다(divide)
    left_half = my_list[:len(my_list)//2]    # 왼쪽 반
    right_half = my_list[len(my_list)//2:]   # 오른쪽 반

    # merge_sort 함수를 재귀적으로 호출하여 부분 문제 해결(conquer)하고,
    # merge 함수로 정렬된 두 리스트를 합쳐(combine)준다
    return merge(merge_sort(left_half), merge_sort(right_half))


# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
