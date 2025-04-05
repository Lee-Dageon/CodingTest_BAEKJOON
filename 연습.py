n = int(input())  # 일 수 입력
line = input()

M = [['.'] * n]  # 최소 행렬 초기화 (1행, n열)
r = 0  # 현재 행 위치 (0부터 시작)
p = '.'  # 이전 기호 저장

for c in range(n):
    if line[c] == '+':
        if p == '/':
            if r == 0:
                M.insert(0, ['.'] * n)  # 맨 위에 새로운 행 추가
            else:
                r -= 1  # 위로 이동
        p = M[r][c] = '/'
    elif line[c] == '-':
        if p == '\\' or p == '_':
            if r == len(M) - 1:
                M.append(['.'] * n)  # 맨 아래에 새로운 행 추가
            r += 1  # 아래로 이동
        p = M[r][c] = '\\'
    else:
        if p == '/':
            if r == 0:
                M.insert(0, ['.'] * n)  # 맨 위에 새로운 행 추가
            else:
                r -= 1  # 위로 이동
        p = M[r][c] = '_'

print(M)
# 행렬 출력
for r in range(len(M)):
    print(''.join(M[r]))
