# 어두운 굴다리 문제
# 굴다리 0~N을 밝히게 가로등 설치
# 가로등을 설치할 개수 M과 각 가로등의 위치 x

# 최소한의 높이로 모든 길을 밝히고자
# H라면 왼쪽으로 H, 오른쪽으로 H


N = int(input())   #5   굴다리 길이
M = int(input())   #2   가로등 개수
x = map(int, input().split())   #가로등의 위치

def check(mid): #mid 높이로 굴다리 전체를 다 비추는가?
    p = 0 #굴다리 시작 위치로 초기화  p = 굴다리 위에서 "다음으로 비춰져야 할 시작 위치
    for light in x:
        if light - p > mid:
            return False
        p = light + mid     #현재 가로등이 비추는 오른쪽 범위로 p설정






result = 0
start = 1
end = N             #N은 굴다리 길이
while start <= end:
    mid = (start+end) // 2
    if check(mid):      #mid 높이로 굴다리 전체를 다 비추는가?
        result = mid
        end = mid - 1   #가로등 높이 낮추기
    else:
        start = mid + 1     #가로등 높이 높이기


print(result)




