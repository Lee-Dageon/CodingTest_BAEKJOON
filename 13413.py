#초기 상태의 말과 목표 상태의 말이 주어질 때,
#목표 상태에 도달할 수 있는 최소 횟수를 구하는 프로그램을 작성하시오.

#처음 문자들과 마지막 다섯 개 문자들을 비교
#블랙->화이트 작업의 수를 세기(왼쪽 B, 오른쪽 W)
#화이트->블랙 작업의 수를 세기(왼쪽 W, 오른쪽 B)

#자리를 바꾼다.
#남는 것은 뒤집는다


# n 입력받기
T = int(input())

# n번 반복하여 각 문자열 입력받기
for _ in range(T):  #T번 반복
    N = int(input())    #말의 개수
    orig = input()
    goal = input()
    BW = 0  #블랙을 화이트로 바꾸는 변수
    WB = 0  #화이트를 블랙으로 바꾸는 변수

    for i in range(N):
        if orig[i] == 'B' and goal[i] == 'W':
            BW += 1

        if orig[i] == 'W' and goal[i] == 'B':
            WB += 1

    print(max(BW, WB))







