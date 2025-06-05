# 특정한 수의 범위 안에 존재하는 모든 소수를 찾을 때
# 에라토스테네스의 체 사용

# 순회강연 문제 1
# 크루스칼 문제 1
# 위상정렬 문제 1
# 소수 판정, 투포인터를 이용해서 순열에서 만족하는 부분수열을 찾는 문제
# 누적값을 이용해 빠르게 계산하는 문제
# 교재에 있는 코드를 그대로 적용하는 문제 많음

# 투 포인터
# 리스트에 담긴 데이터에 순차적으로 접근
# 특정한 합을 가지는 부분 연속 수열 찾기

n = 5   #데이터 개수
m = 5   #찾고자 하는 부분합
data = [1,2,3,2,5] #전체 수열
count = 0

interval_sum = 0    #수열의 부분합
end = 0
#start를 차례로 증가시키며 반복

for start in range(n): #start = 0, 1, 2 ... , n-1
    #end를 가능한 만큼 이동시킨다.
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1

    #부분합이 m이면 count를 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)







