# 회의실 배정
# 회의실 사용표 만들기
# 파이썬 다중정렬
# L.sort(key=lambda)


# N개의 회의
# 회의 I에 대해 시작 끝 시간 주어짐
# 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는
# 회의의 최대 개수
# 시작 == 끝 시간 가능
# 끝나는 시간으로 정렬한 후
# 같은 끝나는 시간이면 시간이 느린 것으로 선택

import sys

input = sys.stdin.readline  # input 함수를 대체
N = int(input())    #회의 개수
meetings = []       #리스트로 저장
for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 끝나는 시간을 오름차순으로 정렬하고
# 시작 시간이 끝나는 시간보다 뒤면서, 종료 시간이 빠른 것을 우선으로 선택


meetings.sort(key=lambda x: (x[1], x[0]))

count = 1       #맨 처음 회의는 무조건 선택
end_time = meetings[0][1]


for i in range(1, len(meetings)):
    if end_time <= meetings[i][0]: #끝나는 시간보다 시작 시간이 크다면
            count += 1
            end_time = meetings[i][1] #끝나는 시간은 다음 걸로 변경

    else:
        continue
print(count)


