# H 층수 W 방수
def reserve(H, W, N): #방 번호를 반환하는 함수
    count = 1
    for room in range(1, W+1): # room = 1, 2, 3 ... W
        for floor in range (1, H+1): #floor = 1, 2, 3 ... H
            if count == N:
                return floor * 100 + room
            count += 1



T = int(input()) #테스트 케이스 개수
for _ in range(T):
    H, W, N = map(int, input().split())
    print(reserve(H, W, N))
