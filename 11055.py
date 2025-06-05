# 수열 A가 주어졌을 때 그 증가하는 부분 수열 중에서 합이 가장 큰 것

# 수열의 크기 N
n = int(input())

# 수열 Ai가 주어짐
array = list(map(int, input().split()))

#합이 가장 큰
#dp 테이블 1로 초기화
#dp[i] : array[i]를 끝 원소로 갖는 증가하는 부분수열의 합
dp = array[:]  #1차원 dp테이블 초기화

#가장 긴 증가하는 부분 수열(LIS) 알고리즘

for i in range(1,n):    #1부터 n-1까지
    for j in range(0,i): #0부터 i-1까지
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+array[i])

for i in range (n):
    print(dp[i],end=" ")
print(max(dp))

#dp테이블 2문제
#이진탐색 1문제
#정렬 1문제
#추가 두문제
