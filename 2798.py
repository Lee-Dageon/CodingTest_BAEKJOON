# 블랙잭
# 카드 개수는 N장
# M을 넘지 않으면서 M 에 최대한 가까운
# 카드 3장의 합 출력

N, M = map(int, input().split())

max_sum = 0

cards = list(map(int, input().split()))

from itertools import combinations

for c in combinations(cards, 3):
    current_sum = sum(c)
    if max_sum < current_sum <= M:
        max_sum = current_sum

print(max_sum)







