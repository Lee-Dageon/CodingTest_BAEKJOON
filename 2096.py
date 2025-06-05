# 내려가기

N = int(input())
dp_max = list(map(int, input().split()))
dp_min = dp_max[:]      #값 복사
for _ in range(N-1):
    array = list(map(int, input().split()))
    p_max = [None] * 3
    p_min = [None] * 3
    for c in range(3):
        if c == 0: up_left_max = 0; up_left_min = 0
        else:       up_left_max = dp_max[c-1]; up_left_min = dp_min[c-1]
        # 왼쪽 위

        up_max = dp_max[c]; up_min = dp_min[c]
        if c == 2: down_left_max = 0; down_left_min = 0
        else:       down_left_max = dp_max[c+1]; down_left_min = dp_min[c+1]


