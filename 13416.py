# 하루에 최대 1개 회사의 주식
# 장이 열릴 때 사고, 그날 장이 닫힐 때 모두 판다
# 수익이 안 날 거 같으면 주식 구매 X
# N = 일수

# 최대 이윤 출력 프로그램

# 테스트 데이터 개수 T
# 주식 데이터의 일수 N

import sys
input = sys.stdin.readline

T = int(input())
result = []

for _ in range (T):
    N = int(input())
    profit = 0
    for _ in range(N):
        test_case = list(map(int, input().split()))
        M = max(test_case)
        if M > 0:
            profit += M

    result.append(str(profit))

print("\n".join(result))





