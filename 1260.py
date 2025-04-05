# N, M, V
# 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호
# 사전 또는 2차원 배열로 구성

# 재귀 DFS, preorder traversal (node->left subtree->right subtree)
# DFS -> BFS : 스택을 큐로만 변경하면 됨.
N, M, V = map(int, input().split())
visited = [False] * (N+1)   #방문 기록


#graph 구현 : adjacency matrix (N+1)X(N+1)    # 2차원 배열
graph = [[False]*(N+1) for _ in range(N+1)]  # 전부 False로 초기화
for _ in range(M):   #M개 간선 입력
    a, b = map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True
print(graph)

# [[False, False, False, False, False],
# [False, False, True, True, True],
# [False, True, False, False, True],
# [False, True, False, False, True],
# [False, True, True, True, False]]

#재귀호출로 구현
def DFS_rec(graph, V, visited):
    print(V, end = '')   #node 탐색
    visited[V] = True    #정점 V 방문 처리
    # 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
    for i in range(1, N+1):
        if graph[V][i] and not visited[i]: #V정점의 인접 i를 방문하지 않았다면
            DFS_rec(graph, V, visited)    #재귀호출


#스택 DFS 구현
from collections import deque # (양방향 큐)
stack = deque([V])      #스택을 deque로 구현
while stack:            #스택이 빌 때까지
    V = stack.pop()     #스택의 제일 뒤에서 꺼낸다.
    if not visited[V]:  #방문하지 않았다면 방문 처리
        print(V, end = '')
        visited[V] = True
    for i in range(N, 0, -1):   #i=N, N-1, .... , 1
        if graph[V][i] and not visited[i]:  #V정점의 인접 i를 방문하지 않았다면
            stack.append(i)                 #제일 뒤에 정점 i 추가







#간선
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4


