# # 음료수 얼려 먹기 문제
# # 완전탐색? -> 방향벡터
# # 특정 지점에서 상, 하, 좌, 우를 살펴봄
# # 0이면서 아직 방문하지 않은 지점 -> 상, 하, 좌, 우 살펴봄
#
# # 세로 길이 n, 가로 길이 m
# n, m = map(int,input().split())
#
# # 2차원 리스트의 맵 정보 입력받기
# graph = [] #리스트
#
#
# #재귀 dfs
# def dfs(r,c):   #r행 c열
#     if 0<=r<n and 0<=c<m:
#         if graph[r][c] == 0:
#             graph[r][c] = 1 #해당 노드 방문처리
#             #상하좌우 재귀 호출
#             for dr, dc in [(-1,0),(1,0)(0,-1),(0,1)]:
#                 dfs(r+dr, c+dc)
#             return True
#     return False
#
# # 모든 노드에 대하여 음료수 채우기(??)
# result = 0
# for i in range(n):
#     for j in range(m):
#         # 현재 위치에서 DFS 수행
#         if dfs(i,j) == True:
#             result += 1





# 미로 탈출 문제
# 괴물이 있으면 0, 없으면 1
# 탈출을 위해 움직여야 하는 최소 칸의 개수


# 문제를 푸는 아이디어
# (1,1) 부터 BFS 수행(큐 이용)
# 상하좌우 탐색해서, 거기에 1이 있으면,
# 숫자를 하나씩 더해가면서 자리를 옮김

# 최단 거리 문제는 bfs를 써야 한다
# dfs => 한 방향으로 끝까지 가 보고,
# 막히면 돌아와서 다른 길 탐색 (백트래킹 필요) [스택 사용]
# bfs => 모든 방향을 한 칸씩 탐색 [큐 사용]


# ✔ 입력받은 미로를 2차원 리스트로 저장
# ✔ BFS를 활용해 탐색 진행 (큐 사용)
# ✔ 현재 칸에서 네 방향(상, 하, 좌, 우)으로 이동
# ✔ 방문 가능한 칸이면 거리 정보(이동 칸 수)를 갱신하며 큐에 추가
# ✔ 출구(N, M)에 도착하면 즉시 거리 출력 (최단 거리)


# 입력 예시
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

# 10

from collections import deque

# 현재 칸에서 네 방향(상, 하, 좌, 우)으로 이동
# 방향벡터 이용(정의)
dr = [-1, 1, 0, 0]  #좌, 우
dc = [0, 0, -1, 1]  #상, 하


# ✔ 방문 가능한 칸이면 (1이면)
# 거리 정보(이동 칸 수)를 갱신하며 큐에 추가
def bfs(r, c):  # r행 c열 위치
    queue = deque([r, c])
    while queue:  # 큐가 빌 때까지
        r, c = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
        #미로 공간을 벗어난 경우 무시
        if nr < 0 or, nr >= n or nc < 0 or nc >=m:
            continue
        #벽인 경우 무시
        if graph[nc][nr] == 0:  #행,열
            continue
        #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
        if graph[nc][nr] == 1:
            graph[nc][nr] = graph[c][r] + 1
            queue.append((nc, nr))

    return graph[n-1][m-1]



# 입력받은 미로를 2차원 리스트로 저장
n, m = map(int, input().split())    #n은 행, m은 열
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

print(graph)
# [[1, 0, 1, 0, 1, 0],
# [1, 1, 1, 1, 1, 1],
# [0, 0, 0, 0, 0, 1],
# [1, 1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1, 1]]




print(bfs(0,0))














