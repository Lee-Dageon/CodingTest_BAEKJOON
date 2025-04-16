# 주어진 항공권을 이용한 여행경로를 짜는 문제



# 재귀 dfs
def DFS(port, path, graph, ports, nTickets):



def solution(tickets):
    # tickets를 조회해서 중복되지 않는 공항 리스트를 알파벳 순서로 생성
    # [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    ports = set()
    for a, b in tickets:
        ports.add(a)
        ports.add(b)

    # [["ICN", "JFK"], ["HND", "IAD"]]
    # 전체 공항 목록

    answer = []
    return answer




