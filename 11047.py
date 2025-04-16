# 동전의 종류 N
# 동전 매우 많이 가지고 있음
# 그 가치를 합 K
# 필요한 동전 개수의 최솟값 구하기
# 그리디 알고리즘

# 첫째 줄에 n과 k가 주어진다

n, k = map(int, input().split())

# 동전의 가치를 오름차순으로 받기
# 그리디는 언제 실패하고 언제 성공하는가?
# 배수면, 작은 동전으로 합친 값을 큰 동전으로 항상 대체 가능


# 동전 가치들을 입력받는다, 오름차순으로 정렬

coins = []
for _ in range (n):
    coins.append(int(input()))
coins.reverse()     #역순으로 정렬

coin_count = 0

for coin in coins:
    if k == 0:
        break
    else:
        coin_count += k // coin     # 4200 // 1000 = 4
        k = k % coin

print(coin_count)




















