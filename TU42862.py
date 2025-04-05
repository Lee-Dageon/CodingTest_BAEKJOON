# 체육복 빌려주는 문제

# reserve 숫자 앞 숫자, 뒷 숫자에 lost와
# 일치하는 숫자가 있다면
# reserve 에서 하나 lost에서 하나 빼고
# count += 1

n = input() #전체 학생 수
lost = list(map(int,input().split()))   #잃어버린 사람
reserve = list(map(int,input().split()))    #여분 체육복 가진 사람

count = n - len(lost)

#여벌 체육복을 가진 학생이 도난당했다면

#체육복이 없는 사람
lost_final = list(set(lost) - set(reserve))
#여벌 체육복이 있는 사람
reserve_final = list(set(reserve) - set(lost))

#전체 학생 수 - 체육복이 없는 사람 = 체육복이 있는 사람!                                                                                                                                                                                                                                                                                                                                     ㅛㅠ
# 체육복이 있는 학생 수
count = n - len(lost_final)

# 여벌 체육복 나눠주기
for r in reserve_final:
    if r - 1 in lost_final:  # 앞 번호 학생이 체육복이 없는 경우
        lost_final.remove(r - 1)
        count += 1
    elif r + 1 in lost_final:  # 뒷 번호 학생이 체육복이 없는 경우
        lost_final.remove(r + 1)
        count += 1

# 결과 출력
print(count)



def solution(n, lost, reserve):
    # 도난당했지만 여벌이 있는 학생 제외
    lost_final = sorted(set(lost) - set(reserve))
    reserve_final = sorted(set(reserve) - set(lost))

    # 체육복을 빌려준 경우 체크
    for r in reserve_final:
        if r - 1 in lost_final:  # 앞번호 학생에게 빌려줌
            lost_final.remove(r - 1)
        elif r + 1 in lost_final:  # 뒷번호 학생에게 빌려줌
            lost_final.remove(r + 1)

    # 체육수업을 들을 수 있는 최대 학생 수
    return n - len(lost_final)




# 1 2 3 4 5
# 도난 : 2 4
# 여벌 : 2 3 4
# 진짜 잃어버린사람 : 0
# 여벌 있는 사람






