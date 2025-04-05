# N개의 도시
# 도로 길이
# 기름 가격 받음


N = input()
length = list(map(int,input().split()))
oilCost = list(map(int,input().split()))
minCost = 0

# 첫번째는 무조건 기름 넣어야함 다음 도시로 갈때까지
# 지금 도시빼고 (나머지 도시-1)를 다 탐색해서
# 더 싼 도시가 있으면 그 도시까지만 넣음
# 없으면 끝까지 여기서 다 넣음

now_cost = oilCost[0]
start = 0
curcity = 0 #현재 도시

m 
for curcity in range (N-1): #마지막 도시는 탐색할 필요 없음
    cheap_cost_index = curcity

    if now_cost > oilCost[i]:
        cheap_cost_index = i
        now_cost = oilCost[cheap_cost_index]
    j = cheap_cost_index

for j in range (i, cheap_cost_index)
    minCost += now_cost * length[j]

    i = cheap_cost_index
    else:
        minCost += now_cost * length[i]


print(minCost)








print(minCost)