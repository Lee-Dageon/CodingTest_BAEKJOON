# 표준 입력으로 A B를 입력받고
# A행 B열 M을 구성(y,x)
# 오른쪽 회전한 R 왼쪽 회전한 L 전치행렬 T를 구한다

def print2D(matrix, A, B):
    for r in range(A):
        for c in range(B):
            # 마지막 열이 아니라면 공백 추가
            if c != B - 1:
                print(matrix[r][c], end=' ')
            else:
                print(matrix[r][c], end='')  # 마지막 열은 공백 없이
        # 마지막 행이 아니라면 줄바꿈 추가
        if r != A - 1:
            print()




# def print2D2(matrix):
#     for row in matrix:
#         print(' '.join(map(str, row)))  # 각 요소를 공백으로 구분하여 출력


A, B = map(int, input().split())     #3 5

#원소가 1씩 증가하는 행렬 M
M = [[(r * B) + c + 1 for c in range(B)] for r in range(A)]

print("M")
print2D(M, len(M), len(M[0]))

# 오른쪽 행렬 R

# 11  6  1
# 12  7  2
# 13  8  3
# 14  9  4
# 15  10  5

R = [[M[r][c] for r in range (A-1, -1, -1)] for c in range(B)]

print()
print("R")
print2D(R, len(R), len(R[0]))



# 왼쪽 회전 L
# L
# 5  10  15
# 4  9  14
# 3  8  13
# 2  7  12
# 1  6  11
# 첫 번째 열이 마지막 행이 됨
# 두 번째 열이 마지막에서 두 번째 행이 됨



L = [[M[r][c] for r in range (A)] for c in range(B-1, -1, -1)]
print()
print("L")
print2D(L, len(L), len(L[0]))

#전치 행렬 T
T = [[M[r][c] for r in range(A)] for c in range(B)]
#c가 열이고 r이 행 x,y값
#열을 기준으로 그 열에 있는 값을 행마다 꺼내서
print()
print("T")
print2D(T, len(T), len(T[0]))
