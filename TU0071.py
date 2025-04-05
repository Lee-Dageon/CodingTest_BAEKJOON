# 십자말 풀이 문제
# A는 가로로 출력
# 일단 모든 칸을 .으로 출력하기
# A와 B를 비교한 후, B에 해당되는 문자 인덱스 행부터 A를 출력
# B에 해당하는
# join 이라는 함수 사용


A, B = input().split()

M = [['.']*len(A) for _ in range(len(B))]

for c in range (len(A)):
    r = B.find(A[c])    #A단어의 c번째 문자를 B단어에서 찾는다. 찾지 못하면 -1 을 반환한다.
    if r != -1:         #찾았으면 r행 c열에서 중복
        for i in range(len(A)):     #r행에 A단어를 넣는다.
            M[r][i] = A[i]

        for i in range(len(B)):     #c열에 B단어를 넣는다.
            M[i][c] = B[i]
        break


for i in range(len(B)):  #행의 개수
    print(''.join(M[i]))

