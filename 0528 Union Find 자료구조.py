# 각 원소의 루트 찾기
def find_parent(parent,x):
    # 루트를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기(두 원소의 루트를 같게)
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드와 간선의 개수 입력
v, e = map(int,input().split())
parent = [0] * (v + 1)    #부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선 정보 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost,a,b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)








# cycle = False # 사이클 발생 여부
#
# for i in range(e):
#     a, b = map(int,input().split())
#     # 사이클이 발생한 경우 종료
#     if find_parent(parent, a) == find_parent(parent, b):
#         cycle = True
#         break
#
#     # 사이클이 발생하지 않았다면 합집합 연산 수행
#     else:
#         union_parent(parent, a, b)
#
#     if cycle:
#         print("사이클이 발생했습니다.")
#
#     else:
#         print("사이클이 발생하지 않았습니다.")



# 신장 트리
# 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프

# 크루스칼 알고리즘
# 대표적인 최소 신장 트리 알고리즘
# 그리디 알고리즘

# 1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다
# 2. 간선을 하나씩 확인하며 현재의 간선이 사이클이 발생하는지 확인
# 3. 모든 간선에 대하여 반복한다


