# 자산 증감 문제
# n일 동안 회사의 순자산을 나타내는 선을 그린다.

# 1단위 증가 +
# 1단위 감소 -
# 동일 유지 =
# 첫날 이전에는 순자산 0
# 무한 행렬에 자산증감 선을 그린다
# 행렬 행의 인덱스는 !!!위쪽으로 증가
# 열의 인덱스는 오른쪽으로 커진다

# 7
# ++---==

N = int(input())    #일 수
LINE = input()      #문자열 입력받기

#2차원 그래프의 열 채우기
graph = [["."] * N]
r = 0               # 현재 행 위치
p = '.'             # 이전 기호 저장

#2차원 그래프의 행 채우기
for c in range(N):          #N(열) 이 늘어날 때마다
    if LINE[c] == '+':
        if p == '/':
            if r == 0:
                graph.insert(0, ['.'] * N)      #리스트의 맨 앞에 행을 추가. 새로 추가된 줄이 0이 됨
        p = graph[r][c] = '/'


    elif LINE[c] == '-':
        if p == '\\' or p == '_':    # 정확한 비교
            if r == len(graph) - 1:
                graph.append(['.'] * N)      #리스트의 맨 뒤에 행을 추가. 새로 추가된 줄이 1이 됨
            r += 1
        p = graph[r][c] = '\\'


    elif LINE[c] == '=':
        if p == '/':
            if r == 0:
                graph.insert(0, ['.'] * N)
        p = graph[r][c] = '_'


for c in range(len(graph)):
    print(''.join(graph[c]))

        



        







