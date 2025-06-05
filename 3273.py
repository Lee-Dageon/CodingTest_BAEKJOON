# # n개의 서로 다른 양의 정수로 이루어진 수열
# # 1 =< 이고 <= 1'000'000 인 자연수
# # 자연수 x가 주어졌을 때 ai + aj = x를 만족하는
# # 쌍의 개수를 구하는 프로그램
#
# n = int(input())    #수열의 개수
# # 수열 주어짐
# # 5 12 7 10 9 1 2 3 11
# arr = list(map(int,input().split()))
# x = int(input())
#
# twopoint_sum = 0
# arr.sort()
#
# start = 0
# end = 1
# count = 0
#
# for start in range(n-1): #start = 0, 1, 2 ... , n-2
#     end = start + 1
#     while end < n:
#         twopoint_sum = arr[start] + arr[end]
#         if twopoint_sum == x:
#             count += 1
#             break
#         elif twopoint_sum > x:
#             break
#         else:
#             end += 1
#
# print(count)


n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
start = 0
end = n - 1
count = 0

while start < end:
    twopoint_sum = arr[start] + arr[end]
    if twopoint_sum == x:
        count += 1
        start += 1
        end -= 1
    elif twopoint_sum < x:
        start += 1
    else:
        end -= 1

print(count)

