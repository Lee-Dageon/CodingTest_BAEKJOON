# 회장 점수 + 회원 점수 계산 후 정렬 및 출력

N = int(input())  # 참가자 수
boss_ranks = list(map(int, input().split()))  # 회장 순위
member_votes = list(map(int, input().split()))  # 협회 회원 투표 수

# 회장 점수 계산
# 회장 점수와 등수의 총합은 항상 N+1 이 되어야 함
boss_scores = [0] * N
for i in range(N):
    boss_scores[i] = (N + 1) - boss_ranks[i]
# ----------------------------------------------------

# 협회 회원 점수 계산
# 회원 점수를 내림차순으로 정렬 후 점수 할당
member_scores = [0] * N
votes_with_index = [(member_votes[i], i) for i in range(N)]  # (투표 수, 참가자 번호)

votes_with_index.sort(reverse=True, key=lambda x: x[0])  # 투표 수에 따른 내림차순 정렬

for rank, (_, index) in enumerate(votes_with_index):
    member_scores[index] = N - rank  # 높은 순위부터 N부터 차감하며 할당


# 총점 계산 및 참가 번호 포함
participants = []
for i in range(N):
    total_score = boss_scores[i] + member_scores[i]  # 총점 = 회장점수+회원점수
    participants.append((total_score, member_scores[i], i))  # (총점, 회원 점수, 참가자 번호)

# 총점과 협회 회원 점수 기준으로 내림차순 정렬
participants.sort(key=lambda x: (-x[0], -x[1]))


# 결과 출력
for rank, (total, _, code_number) in enumerate(participants, start=1):
    print(f"{rank}. Kod{code_number+1:02} ({total})")