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









# dfs, bfs 구현
from collections import deque

# 입력 받기
N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

# 간선 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호가 작은 순서로 탐색하기 위해 정렬
for i in range(1, N + 1):
    graph[i].sort()


# DFS 구현
def dfs(v, visited):
    visited[v] = True
    print(v, end=' ')
    for next_node in graph[v]:
        if not visited[next_node]:
            dfs(next_node, visited)


# BFS 구현
def bfs(start):
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for next_node in graph[v]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)


# 실행
visited_dfs = [False] * (N + 1)
dfs(V, visited_dfs)
print()
bfs(V)





#숨바꼭질 문제
from collections import deque

def hide_and_seek(N, K):
    MAX = 100001
    visited = [0] * MAX  # 방문 및 시간 저장

    queue = deque()
    queue.append(N)

    while queue:
        current = queue.popleft()

        if current == K:
            return visited[current]

        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos < MAX and visited[next_pos] == 0:
                visited[next_pos] = visited[current] + 1
                queue.append(next_pos)


# 입력
N, K = map(int, input().split())
print(hide_and_seek(N, K))








# 중요한 교차로
# 스택을 이용한 DFS 구현
from collections import deque  # 리스트보다 시간복잡도가 낮다


def DFS(V, i, graph, N, visited):
    stack = deque([V])
    while stack:  # 스택이 빌 때까지
        V = stack.pop()  # 스택 제일 뒤에서 꺼냄
        if not visited[V]:  # 방문하지 않았다면
            visited[V] = True  # 방문 처리
            for j in range(1, N + 1):
                # i가 아니고 방문하지 않았고 V와 연결되었으며 스택에 없다면
                if j != i and not visited[j] and graph[V - 1][j - 1]:
                    stack.append(j)


# 입력 처리
N, M = map(int, input().split())  # N은 교차로 수, M은 도로 수
graph = [[False for _ in range(N)] for _ in range(N)]  # N*N 2차원 그래프 graph[i][j] : i-j 도로가 존재하면 True 아니면 False
for _ in range(M):  # M개 도로(간선)에 대해서 graph 설정
    i, j = map(int, input().split())
    graph[i - 1][j - 1] = True  # 교차로 번호는 1 ... N -> 인덱스 0...N-1로 변경
    graph[j - 1][i - 1] = True

answer = []  # 중요한 교차로 목록

# 각 교차로를 하나씩 제거하며 확인
for i in range(1, N + 1):
    visited = [False] * (N + 1)  # 방문 배열 초기화 (1-indexed)
    components = 0  # 연결 요소의 개수

    # 모든 교차로에 대해 DFS 탐색
    for j in range(1, N + 1):
        if j != i and not visited[j]:  # 제거된 교차로 i를 제외한 DFS 탐색
            DFS(j, i, graph, N, visited)
            components += 1

    # 제거한 교차로로 인해 연결 요소가 증가하면 중요한 교차로로 간주
    if components > 1:
        answer.append(i)

# 결과 출력
print(len(answer))  # 중요한 교차로 개수
for crossroad in answer:
    print(crossroad)





#항공권 문제
def solution(tickets):
    from collections import defaultdict         #딕셔너리의 기본값 설정 가능
    tickets.sort()  # 알파벳 순서 우선 탐색을 위해 정렬

    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)

    route = []  # 최종 경로

    def dfs(curr, path):
        if len(path) == len(tickets) + 1:
            route.append(path)
            return True  # 경로 완성 시 바로 종료

        if curr in graph:
            for i in range(len(graph[curr])):
                next_airport = graph[curr].pop(i)  # 티켓 사용
                if dfs(next_airport, path + [next_airport]):
                    return True
                graph[curr].insert(i, next_airport)  # 사용한 티켓 복구 (백트래킹)

        return False

    dfs("ICN", ["ICN"])
    return route[0]









#이진 트리 순회
import sys
input = sys.stdin.readline      #빠른 input

# 트리 저장용 딕셔너리
tree = {}

# 입력 처리
n = int(input())
for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

# 전위 순회: Root - Left - Right
def preorder(node):
    if node == ".":
        return ""
    return node + preorder(tree[node][0]) + preorder(tree[node][1])

# 중위 순회: Left - Root - Right
def inorder(node):
    if node == ".":
        return ""
    return inorder(tree[node][0]) + node + inorder(tree[node][1])

# 후위 순회: Left - Right - Root
def postorder(node):
    if node == ".":
        return ""
    return postorder(tree[node][0]) + postorder(tree[node][1]) + node

# 결과 출력
print(preorder('A'))
print(inorder('A'))
print(postorder('A'))







# 입력 처리
N = int(input())  # 좌석 수
seat_sequence = input().strip()  # 좌석 배열

# 러브시트('LL')를 하나로 처리
compressed_seats = seat_sequence.replace("LL", "L")

# 컵홀더 개수는 항상 좌석 압축 길이에 +1
max_holders = len(compressed_seats) + 1

# 최대값은 좌석 수(N)와 컵홀더 개수 중 작은 값
print(min(N, max_holders))




# 입력 처리
N = int(input())  # 좌석 수
seat_sequence = input().strip()  # 좌석 배열

# 그리디 알고리즘으로 컵홀더 계산
holders_used = 0  # 사용할 수 있는 컵홀더 수
i = 0  # 좌석 탐색용 인덱스

while i < N:        # 좌석 수를 탐색
    if seat_sequence[i] == 'S':  # 일반석
        holders_used += 1
        i += 1  # 다음 좌석으로 이동
    elif seat_sequence[i] == 'L':  # 러브시트
        holders_used += 1  # 한 쌍의 러브시트에 대해 컵홀더 1개 추가
        i += 2  # 러브시트는 쌍으로 묶여 있으므로 2칸 앞으로 이동

# 컵홀더의 최대치는 좌석 수(N)와 holders_used 중 작은 값
print(min(N, holders_used + 1))




코드 설명
탐색 기준
seat_sequence를 왼쪽에서 오른쪽으로 탐색하며:
'S'일 경우 컵홀더를 1개 증가시키고 다음 좌석으로 이동.
'L'일 경우 러브시트 쌍에 대해 컵홀더를 1개 증가시키고 2칸 앞으로 이동(러브시트는 항상 쌍으로 주어짐).
러브시트 쌍이 끝나더라도 컵홀더는 여전히 하나만 추가되므로 효율적으로 관리됩니다.
컵홀더 초과 사용 방지
holders_used+1은 좌우 측면에 항상 하나씩 더 추가할 수 있는 컵홀더를 고려한 값입니다.
결과적으로 좌석 수(N)보다
큰 경우를 방지하기 위해 min()을 사용하여 최댓값을 제한합니다.





# 입력 처리
n = int(input())  # 참가자 수
chairman_ranks = list(map(int, input().split()))  # 회장의 순위 리스트
member_votes = list(map(int, input().split()))  # 협회 회원 투표 수

# 1. 회장이 부여한 점수 계산
chairman_scores = [0] * n
for i in range(n):
    chairman_scores[chairman_ranks[i] - 1] = n - i  # i번째 코드의 점수

# 2. 총점 계산 및 데이터 구성
participants = []  # 참가자 데이터 저장: (총점, 회원 점수, 코드 번호)
for i in range(n):
    total_score = chairman_scores[i] + member_votes[i]
    participants.append((total_score, member_votes[i], i + 1))

# 3. 정렬: 총점(내림차순), 회원 점수(내림차순)
participants.sort(key=lambda x: (-x[0], -x[1]))

# 4. 결과 출력
for rank, (total, member_vote, code_number) in enumerate(participants, start=1):
    print(f"{rank}. Kod[{code_number:02}] ({total})")






# 입력 처리
n = int(input())  # 참가자 수
chairman_ranks = list(map(int, input().split()))  # 회장의 순위 리스트
member_votes = list(map(int, input().split()))  # 협회 회원 투표 수

# 1. 회장이 부여한 점수 계산
chairman_scores = [0] * n
for i in range(n):
    chairman_scores[chairman_ranks[i] - 1] = n - i  # i번째 코드의 점수

# 2. 협회 회원 점수 계산
# 회원 점수 내림차순 정렬 및 점수 할당
member_scores = [0] * n
votes_with_index = [(member_votes[i], i) for i in range(n)]  # (투표 수, 참가자 번호)
votes_with_index.sort(reverse=True, key=lambda x: x[0])  # 투표 수에 따른 내림차순 정렬

for rank, (_, index) in enumerate(votes_with_index):
    member_scores[index] = n - rank  # 높은 순위부터 N부터 차감하며 할당

# 3. 총점 계산 및 데이터 구성
participants = []  # 참가자 데이터 저장: (총점, 회원 점수, 코드 번호)
for i in range(n):
    total_score = chairman_scores[i] + member_scores[i]
    participants.append((total_score, member_scores[i], i + 1))

# 4. 정렬: 총점(내림차순), 회원 점수(내림차순)
participants.sort(key=lambda x: (-x[0], -x[1]))

# 5. 결과 출력
for rank, (total, member_score, code_number) in enumerate(participants, start=1):
    print(f"{rank}. Kod[{code_number:02}] ({total})")



# 협회 회원 점수 계산
# 회원 점수를 내림차순으로 정렬 후 점수 할당
member_scores = [0] * N

# 입력 데이터의 길이가 N과 다른 경우 오류 처리
if len(member_votes) != N:
    raise ValueError("member_votes 리스트의 길이는 N과 같아야 합니다.")



# 결과 확인을 위한 디버깅 출력 (필요 시 제거 가능)
print("정상적으로 계산된 member_scores:", member_scores)









