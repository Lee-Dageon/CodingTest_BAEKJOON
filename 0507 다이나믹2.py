# 병사 배치하기 문제
# 부분 수열 문제
# N명의 병사 무작위 나열
# 특정한 값의 전투력 보유
# 전투력 순으로 내림차순 배열
# 특정한 위치에 있는 병사를 열외시키는 방법 사용
# 남아 있는 병사의 수를 최대

# 다이나믹 프로그래밍 사용
# 문제 해결 아이디어

# 가장 긴 증가하는 부분 수열

# 가장 긴 감소하는 부분 수열을 찾는 문제로 치환

# 점화식 사용
# D[i] = max(D[i], D[j]+1) if array[j] < array[i]

n = int(input())
array = list(map(int, input().split()))
#순서를 뒤집는다. LIS 문제로 전환
array.reverse()
#dp 테이블 1로 초기화
#dp[i] : array[i]를 끝 원소로 갖는 LIS 길이
dp = [1]*n  #1차원 dp테이블 초기화

#가장 긴 증가하는 부분 수열(LIS) 알고리즘

for i in range(1,n):    #1부터 n-1까지
    for j in range(0,i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)


#i가 1이면 j를 0부터 0까지 비교
#i가 2이면 j를 0부터 1까지 비교
print(n-max(dp))
