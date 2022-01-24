'''
3. 알고리즘 패러다임
   1)Brute Force
        (5) 가까운 매장 찾기
        튜플로 주어진 매장들 중 가장 가까운 매장 두개를 찾아 리턴하기
        ex)
        튜플은 각 매장의 위치를 x, y 좌표로 나타낸 것입니다. 
        0번 매장은 (2, 3)에, 그리고 1번 매장은 (12, 30) 위치에 있는 거죠.
        태호가 사용하려는 함수 closest_pair는 이 좌표 리스트를 파라미터로 받고, 
        리스트 안에서 가장 가까운 두 매장을 [(x1, y1), (x2, y2)] 형식으로 리턴합니다.
        참고로 태호는 이미 두 좌표 사이의 거리를 계산해 주는 함수 distance를 써 놨는데요, 
        함수 distance는 인풋으로 두 튜플을 받아서 그 사이의 직선 거리를 리턴합니다.
'''

# 제곱근 사용을 위한 sqrt 함수
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
# 윤아코드
def closest_pair(coordinates):
    storeCnt = len(coordinates)
    storeA, storeB = (0, 0), (0, 0)
    minDistance = distance(coordinates[0],coordinates[1]);
    for i in range (0, storeCnt-1):
        for j in range (i+1, storeCnt):
            newDistance = distance(coordinates[i], coordinates[j])
            if minDistance > newDistance:
                minDistance = newDistance
                storeA = coordinates[i]
                storeB = coordinates[j]
    return [storeA, storeB]
                

#지수답
def closest_pair(test_coordinates):
    minDistance = 100
    for i in range(0, 5):
        for j in range(i+1, 6-i):
            newDistance = distance(test_coordinates[i], test_coordinates[j])
            if minDistance> newDistance:
                minDistance = newDistance
                a = test_coordinates[i]
                b = test_coordinates[j]
    return [a, b]


#해설코드
def closest_pair(coordinates):
    # 현재까지 본 가장 가까운 두 매장
    pair = [coordinates[0], coordinates[1]]
  
    for i in range(len(coordinates) - 1):
        for j in range(i + 1, len(coordinates)):
            store1, store2 = coordinates[i], coordinates[j]

            # 더 가까운 두 매장을 찾으면 pair 업데이트
            if distance(pair[0], pair[1]) > distance(store1, store2):
                pair = [store1, store2]

    return pair





# 테스트
coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(coordinates))

#출력결과 [(2, 3), (3, 4)]
