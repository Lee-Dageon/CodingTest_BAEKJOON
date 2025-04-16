# from collections import deque #빠른 속도를 원할 때(시간에 민감한 코딩테스트 문제)
#
# from 연습 import visited

# stack = []
# stack = deque()
# print(stack)

# queue = deque()

# def recursive_function(i):
#     if i == 100:
#         return
#     print(i,'번째 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
#     recursive_function(i+1)
#     print(i, '번째 함수를 종료합니다.')
#
# recursive_function(1)

# 팩토리얼 구현 예제




# # DFS 소스코드 재귀함수 예제
# def dfs(graph, v, visited): #그래프, 현재노드, 방문여부
#     visited[v] = True   #현재 노드를 방문 처리
#     print(v, end = '')
#     #현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[v]:
#         if not visited[i] :
#             dfs(graph, i, visited)
#
#
# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]


# #각 노드가 방문된 정보를 표현
# visited = [False] *9
#
# dfs(graph, 1, visited)



# #BFS
# from collections import deque
#
#
# def bfs(graph, start, visitid):
#     queue = deque([start])
#
#     visited[start] = True
#
#
#     while queue:    #큐가 빌 때까지
#         v = queue.popleft()     #큐에서 하나의 원소를 뽑아 출력
#         print(v,end = '')
#         #아직 방문하지 않은 인접한 원소들을 큐에 삽입
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#
# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]
#
# visited = [False] * 9
# bfs(graph, 1, visited)


# 4 5
# 00110
# 00011
# 11111
# 00000

# 음료수 얼려 먹기
# 아이스크림 개수 구하기
#
# N, M = map(int, input().split())    #4,5
# # 얼음 틀 입력받기 (2차원)
# ice_map = [list(map(int, input())) for _ in range(N)]



#문제 해결 아이디어
#상 하 좌 우를 살펴보고 주변에 값이 0이면서 아직 방문하지
#않은 지점이 있다면 해당 지점을 방문

#하나의 dfs가 끝날 때마다 아이스크림 카운트 증가
#방향벡터 (완전탐색)

#
#
# #상, 하, 좌, 우 방향벡터
# dr = [0, 0, -1, 1] #상, 하 y  행   N
# dc = [-1, 1, 0, 0] #좌, 우 x  열   M
#
# visited = [[False] * M for _ in range (N)]
# ice_cream_count = 0
#
#
#
# #y * x로 받는다고 생각하면 쉬움
#
#
# def dfs(r, c):      #행, 열
#
#     visited[r][c] = True        #방문한 곳은 True
#
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#
#         if 0 <= nr < N and 0 <= nc < M:
#             if ice_map[nr][nc] == 0 and not visited[nr][nc]:
#                 dfs(nr, nc)         #재귀함수로 구현
#
#
#
#
#
# #모든 칸을 돌며 dfs 실행
# for r in range (N):
#     for c in range(M):
#         if visited[r][c] == False and ice_map[r][c] == 0:
#             dfs(r, c)
#             ice_cream_count += 1
#
# # print(f"visiting r={r}, c={c})
#
# print(ice_cream_count)




# 미로 탈출
# NXM 직사각형 형태의 미로   YxX
# 겜공이의 위치 (1,1)
# 괴물이 있으면 0 없으면 1
# 탈출하기 위해 움직여야 하는 최소 칸
# 시작 칸과 마지막 칸은 항상 1


# 최소 칸 -> BFS(층별로 넓게 퍼져나가는, 큐로 구현)

# 상하좌우 탐색해서
# 주변에 1이 있으면 거기로 이동



N, M = map(int, input(). split())   #y,x
miro = [list((map(int, input()))) for _ in range (N)]
count_to_move = 0

#print(miro)
from collections import deque
# 방향 벡터 이용
# 상, 하, 좌, 우
dr = [-1, 1, 0, 0] #상, 하 y  행   N
dc = [0, 0, -1, 1] #좌, 우 x  열   M



def bfs(r,c):

        queue = deque()
        queue.append((r,c))     #첫 좌표 넣기

        if miro[r][c] == 1:
                visited = [[False] * M for _ in range(N)]

        while queue: #큐가 빌 때까지
                for i in range (4):
                        nr = r + dr[i]
                        nc = c + dc[i]
                if nr >= N or nr < 0 or nc >= M or nc < 0:
                        continue                        #범위 벗어나면 무시

                #벽인 경우 무시
                if miro[nr][nc] == 0:
                        continue

                #변수를 1 증가시킬 수도 있고, visited를 이용하는 방법도 있음
                #visited 이용해 보기
                if miro[nr][nc] == 1 and visited[nr][nc] == False:
                        visited[nr][nc] = True
                        queue.append((nr,nc))




print(count_to_move)

















































