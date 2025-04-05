# 균형 잡힌 영양소

# 3
# 30 20 10
# 10 30 15
# 15 15 25
# 80 20 40 2000


from itertools import combinations

N = int(input()) #음식의 개수

foods = [list(map(int,input().split())) for _ in range(N)]
# 각 음식마다 탄수화물, 단백질, 지방
#print(foods)
#[30, 20, 10]
#[10, 30, 15]
#[15, 15, 25]

gijun = list(map(int, input().split())) #탄수화물, 단백질, 지방, 열량 기준
#[80, 20, 40, 2000]

# print(list(combinations(foods,2)))

count = 0

for i in range(1,4):
    if i > N:
        break
    for food_comb in combinations(foods, i):
        tan, dan, gi, cal = 0, 0, 0, 0
        for food in food_comb:
            tan += food[0]
            dan += food[1]
            gi += food[2]
            cal += food[0]*4 + food[1]*4 + food[2]*9
        if (tan <= gijun[0] and dan >= gijun[1] and gi <= gijun[2]
                and cal <= gijun[3]):
            count += 1



print(count)






