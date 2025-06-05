def solution(N, stages):
    # 각 스테이지에 도달한 유저 수를 세기 위한 배열
    user_count = [0] * (N + 1)

    # stages 배열을 돌면서 각 스테이지에 도달한 유저 수를 세기
    for stage in stages:
        if stage <= N:
            user_count[stage - 1] += 1

    # 전체 유저 수
    total_users = len(stages)

    # 실패율을 계산할 리스트
    failure_rate = []

    for i in range(N):
        if total_users == 0:  # 만약 도달한 유저가 없다면 실패율은 0
            rate = 0
        else:
            rate = user_count[i] / total_users
        failure_rate.append((i + 1, rate))  # (스테이지 번호, 실패율)
        total_users -= user_count[i]  # 해당 스테이지를 거친 유저는 제외

    # 실패율을 기준으로 내림차순 정렬 (실패율이 같으면 스테이지 번호가 작은 것부터)
    failure_rate.sort(key=lambda x: (-x[1], x[0]))

    # 정렬된 스테이지 번호를 리스트에 담아서 반환
    return [stage for stage, rate in failure_rate]

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
