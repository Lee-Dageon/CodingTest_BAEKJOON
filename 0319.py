# 2. 그리디 & 구현 0319


# n = 1260
# count = 0
# #큰 단위동전부터 차례로 확인
# coinTypes = [500, 100, 50, 10]
# for coin in coinTypes:
#     n // coin #해당 동전으로 거슬러 줄 수 있는 동전 개수
#     count += 1
#     n %= coin
#     print(coin, "원 동전 : ", count, "개")
#     if n == 0:
# #         break
# #
# # print(count)
#


# # 1이 될 때까지
# n, k = map(int, input().split())
# result = 0
# while True:
#     #n이 k로 나누어 떨어지는 수가 될 때까지 1을 뺀다
#     target = (n//k)*k
#     result += (n-target)
#     n = target
#
#     #n이 k보다 작을 때(더 이상 나눌 수 없는 경우)
#     if n < k:
#         break
#
#     #k로  나누기
#     result += 1
#     print('n=', n, "target=", target, "result = ", result)
#     n //= k
#
# #마지막 남은 수에 대해서 1씩 빼기
# result += (n-1)
# print(result)

# 곱하기 혹은 더하기
# data = input() # 숫자 문자열 입력 '02987'
#
# result = int(data[0])
# for i in range(1, len(data)):
#     # 두 수 중에서 하나라도 0, 1 인 경우 +를 해야 한다
#     point = int(data[i])
#     if result <= 1 or point <= 1:
#         result += point
#     else:
#         result *= point
# print(result)


# 모험가 길드 문제
# 5
# 2 3 1 2 2
# n = int(input())
# data = list(map(int, input().split()))
# # 공포도 순으로 오름차순 정렬
# data.sort()
# result = 0  #그룹의 총 수
# count = 0  #현재 그룹의 모험가 수
#
# for i in data: #공포도를 낮은 것부터 하나씩 확인
#     count += 1 #현재 그룹에 해당 모험가 포함
#     if count >= i:
#         result += 1 #총 그룹의 수 증가
#         count = 0 #현재 그룹에 포함된 모험가의 수 초기화
#
# print(result)


# # 시뮬레이션 유형(방향벡터 이용)
#
# # N 입력
# n = int(input())
# r, c = 1, 1 #r=row 행, c=column 열
# plans = input().split() #['R', 'R', 'R', 'U', 'D', 'D']
# #L, R, U, D 방향 벡터
# dr = [0, 0, -1, 1]
# dc = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']
# #이동 계획 하나씩 확인
# for plan in plans:  #p`lan = 'R', 'R' ... 'D'
#     #이동 후 좌표 구하기
#     i = move_types.index(plan)  #plan을 찾아서 인덱스 반환
#     nr = r + dr[i]
#     nc = c + dc[i]
#     if 1 <= nr <= n and 1 <= nc <= n:
#         r, c = nr, nc
#
# print(r, c)



# # 시간 탐색
# # 00시 00분 00초부터 N시 59분 59초까지 3이 들어간 경우의 수
# N = int(input())
# count = 0
# for h in range (N + 1): #h = 0, 1, 2, ... n
#     for m in range(60):
#         for s in range(60):
#             if '3' in str(h)+str(m)+str(s):
#                 count += 1
#
# print(count)


# # 왕실의 나이트 문제
# # 나이트 이동 경우의 수 구하기
# # 시뮬레이션, 완전탐색 : 방향 벡터 이용
#
# where = input()
# r = int(where[1])   #행
# c = ord(where[0]) - ord('a') + 1      #열
# # 8가지 방향 벡터 정의
# steps = \
#     [(-2, -1) , (-2, 1), (2, 1), (2, -1),
#      (1, 2), (-1, 2),(-1, -2), (1, -2)]
#
# # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
# result = 0
# for step in steps:
#     # 이동하고자 하는 위치 확인
#     next_c = c + step[0]
#     next_r = r + step[1]
#
#     if next_c >= 1 and next_c <=8 and next_r >= 1 and next_r <= 8:
#         result += 1
#
# print(result)






# #문자열 숫자 문제
# data = input()  # 문자열로 입력
# result = [] # 알파벳 문자들을 갖는 리스트
# value = 0 # 숫자의 합
#
# # 문자를 하나씩 확인
# for x in data:
#     if x.isalpha():
#         result.append(x)    # 알파벳이면
#     else:
#         value += int(x)     # 숫자이면 합산
#
# result.sort()       # 오름차순 정렬
# set(result)
# # 중복 삭제하려면 집합과 리스트 형변환 이용
# if value != 0:
#     result.append(str(value)) #문자로 변환해서 다같이 출력
#
# #result = ['A','K','Z', '34']
# print(''.join(result))









