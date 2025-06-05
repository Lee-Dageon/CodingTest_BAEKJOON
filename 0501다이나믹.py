# # 다이나믹 프로그래밍
# # 효율적인 화폐 구성
#
# # N, M
# # N개의 줄에는 화폐의 가치
# # M을 만들기 위한 최소한의 화폐 개수
#
# # ai : 금액 i를 1로 만들기 위한 최소한의 화폐 개수
# # k : 각 화폐의 단위
#
# # ai = min(ai, ai-k + 1) for 모든 k화폐에 대해서
# n, m = map(int, input().split())
#
# # n개 화폐 단위 입력
# array = [int(input()) for _ in range(n)]
#
# # dp 테이블 초기화
# d = [10001] * ( m + 1 )
#
# # 다이나믹 프로그래밍 진행
# d[0] = 0
# for i in range(n):  # 모든 화폐 종류에 대해서
#     for j in range(array[i], m+1):  # 현재 화폐 인덱스부터 끝까지
#         if d[j - array[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
#             d[j] = min(d[j], d[j-array[i]] + 1)
#
# if d[m] == 10001:
#     print(-1)
# else:
#     print(d[m])







# 금광 문제
# n * m 크기의 금광 (y * x)

# m - 1번에 걸쳐서 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동
# 채굴자가 얻을 수 있는 금의 최대 크기

# 이게 왜 다이나믹 프로그래밍이지?
# array[i][j] = i행 j열에 존재하는 금의 양
# dp[i][j]= i행 j열까지의 최적의 해(얻을 수 있는 금의 최댓값)
# 점화식
# dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])

# 테이블에 접근할 때마다 리스트의 범위를 벗어나지 않는지 체크


for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    dp = []
    index = 0
    for i in range(n):
        # 2차원 DP 테이블 초기화
        dp.append(array[index:index+m])
        index += m

    for j in range(1, m):       #1열부터 m-1열까지 진행
        for i in range(n):      #dp[i][j] 를 갱신하려고 한다.
            # 왼쪽 위
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]




