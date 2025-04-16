#선택정렬(min값 선택)
# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# for i in range(len(array)): #i = 0,1,2,...len(array)
#     min_index = i   #가장 작은 원소의 인덱스
#     for j in range(i+1, len(array)):
#         if array[min_index] > array[j]:
#             min_index = j
#     array[i], array[min_index] = array[min_index], array[i]
# print(array)

#삽입정렬(정렬된 것으로 간주)
# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# for i in range(1, len(array)): #첫 번째 원소는 정렬되어 있다고 판단
#     for j in range(i, 0, -1):   #인덱스 i부터 1까지 1씩 감소하며 반복하는 루프
#         if array[j] < array[j-1]:
#             array[j], array[j-1] = array[j-1], array[j] #스왑
#         else:
#             break
#
# print(array)

# #quick sort(파이썬의 장점을 살린 방식)
# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# def quick_sort(array):
#     if len(array) <= 1: #대상 배열 크기가 1 이하이면 종료
#         return array
#     pivot = array[0]
#     tail = array[1:]
#
#     #python의 list comprehension 기법
#     left_side = [x for x in tail if x<= pivot]
#     right_side = [x for x in tail if x > pivot]
#
#     #분할 후 왼쪽 그룹과 오른쪽 그룹을 각각 정렬한 후 합쳐서 반환
#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)
#
# print(quick_sort(array))


#계수 정렬(제한된 조건에서만 사용 가능)
#데이터 크기 범위가 작고 중복 데이터가 많을 때 효과적
#정수 형태로 표현할 수 있을 때


array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = ' ')  #띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력





