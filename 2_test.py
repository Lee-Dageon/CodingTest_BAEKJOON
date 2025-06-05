# 입력
# 카드 개수, 조커 카드 개수
n, m = map(int, input().split())
cards = input().strip()

# 각각의 문자 개수 세기
d = cards.count('d')
k = cards.count('k')
o = cards.count('o')
r = cards.count('r')
print(d, k, o, r)

max_score = 0

# 조커를 4개의 알파벳에 나누는 모든 경우 탐색
for d_jokers in range(m + 1):  # d에 할당한 조커 개수 (0부터 m까지)
    for k_jokers in range(m - d_jokers + 1):  # k에 할당한 조커 개수
        for o_jokers in range(m - d_jokers - k_jokers + 1):  # o에 할당한 조커 개수
            r_jokers = m - d_jokers - k_jokers - o_jokers  # r에 남은 조커 개수

            # 각 문자별 갱신된 개수
            new_d = d + d_jokers
            new_k = k + k_jokers
            new_o = o + o_jokers
            new_r = r + r_jokers

            #(k개수 2개, o개수 2개, r개수 1개, d개수 1개) 세트이면 세트당 7점 추가
            #
            sets = min(new_k // 2, new_o // 2, new_r, new_d)
            #print(sets)

            # 점수 계산
            score = (new_d ** 2) + (new_k ** 2) + (new_o ** 2) + (new_r ** 2) + (sets * 7)

            # 최대 점수 업데이트
            if score > max_score:
                max_score = score


# 출력
print(max_score)

