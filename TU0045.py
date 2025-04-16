# 중요한 교차로
# 입력의 첫 번째 줄에는 두 개의
# 정수N과M이있습니다
# N은 시흥시의 교차로 수(버텍스)
# 이고 M은 도로 수(간선)입니다.
# 교차로의 번호는 1,2, ...,N이라고 가정합니다.
# 다음M개 줄(2, ...,M+1번째 줄)은
# 시흥시의 도로를 나타냅니다.
# i+1번째 줄은 도로 i로 연결된
# 교차로 쌍을 나타내는
# 1, ...,N범위의 두 정수를 포함합니다.
# N≤ 300, M≤ 50000 입니다.


# 스택을 이용한 DFS 구현
from collections import deque   #리스트보다 시간복잡도가 낮다
def DFS(V, i, graph, N, visited):
    stack = deque([V])
    while stack:                # 스택이 빌 때까지
        V = stack.pop()         # 스택 제일 뒤에서 꺼냄
        if not visited[V]:      # 방문하지 않았다면
            visited[V] = True   # 방문 처리
            for j in range(1,N+1):
                # i가 아니고 방문하지 않았고 V와 연결되었으며 스택에 없다면

N, M = map(int, input().split())    #N은 교차로 수, M은 도로 수
graph = [[False*N for _ in range(N)]]   #N*N 2차원 그래프 graph[i][j] : i-j 도로가 존재하면 True 아니면 False
for _ in range(M): # M개 도로(간선)에 대해서 graph 설정
    i, j = map(int, input().split())
    graph[i-1][j-1] = True  #교차로 번호는 1 ... N -> 인덱스 0...N-1로 변경
    graph[j-1][i-1] = True

answer = [] #중요한 교차로 목록








