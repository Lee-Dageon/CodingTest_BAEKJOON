# 8×8 체스판에서 흰색 칸 위에 있는 'F' 말의 개수를 세는 프로그램


count = 0 # 흰색 칸 위의 말의 개수
flag = True # T F T F ... 토글
for _ in range(8): # 8번 입력
    L = input() # L = '.F.F...F'
    for i in range(8):
        if flag:    # 짝수번 인덱스 = 흰색
            if i%2 == 0 and L[i] == 'F':
                count += 1
        else:
            if i%2 == 1 and L[i] == 'F':
                count += 1
    flag = not flag # T F T F ... 토글
print(count)




