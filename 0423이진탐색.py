# #이진 탐색 재귀 함수
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start+end)//2
#     #찾은 경우 중간점 인덱스 반환
#     if array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
#     else:
#         return binary_search(array, target, mid + 1, end)
#
#
# #이진 탐색을 반복문으로 구현(더 정형화된 코드)
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#              end = mid - 1
#         else:
#             start = mid + 1
#     return None
#
# #재귀적 용법
# n, target = map(int, input().split())
# #정렬된 전체 원소를 입력받기
# array = list(map(int, input().split()))
# #이진 탐색 수행 결과 출력
# result = binary_search(array,target,0,n-1)
# if result == None:
#     print("원소가 존재하지 않습니다")
# else:
#     print(result+1)


# # 값이 특정 범위에 속하는 데이터 개수 구하기
# from bisect import bisect_left, bisect_right
#
# def count_by_range(a, left_value, right_value):
#     right_index = bisect_right(a, right_value)
#     left_index = bisect_left(a, left_value)
#     print(right_index, left_index)
#     return right_index - left_index
#
# a = [1, 2, 3, 3,3,3,4,4,8,9]
# #값이 4인 데이터 개수 출력
# print(count_by_range(a,4,4))
#
#
# #값이 [-1,3]범위에 있는 데이터 개수 출력
# print(count_by_range(a,-1, 3))


#파라메트릭 서치
#최적화 문제를 결정 문제(예, 아니오)로 바꾸어 해결하는 기법
#파라메트릭 서치 문제 -> 이진 탐색을 이용하여 해결

# 떡볶이 떡 문제
# 떡의 개수 N, 요청한 떡의 길이 M
# 떡의 개별 높이

# 4 6
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

# 떡 배열
cake = list(map(int, input().split()))
#이진 탐색을 위한 시작점과 끝점 결정
start = 0
end = max(cake)

# 이진 탐색 수행(반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start+end)//2
    # 잘렸을 때의 떡의 양 계산
    for x in cake:
        if x > mid:
            total += x - mid

    #떡의 양이 부족한 경우 더 많이 자르기
    if total < M:
        end = mid - 1
    #떡의 양이 충분한 경우 덜 자르기
    else:
        result = mid
        start = mid + 1

print(result)








