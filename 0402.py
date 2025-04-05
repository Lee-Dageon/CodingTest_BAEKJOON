from collections import deque   #스택이나 큐를 빠르게 구현
#2차원 배열로 구현한 후 True False로 구현해보자

def dfs_stack(graph, v, visited):
    stack = deque([v])    #스택을 deque으로 구현
    while stack:        #스택이 빌 때까지 계속
        v = stack.pop() #제일 뒤에서 꺼낸다.
        if not visited[v]:
            print(v,end = '')
            visited[v] = True   #해당 정점 v 방문  처리
        #v의 인접노드들을 번호가 큰 것부터 스택에 삽입
        for i in graph[v][::-1]: #번호가 큰 것부터 반대로
            if not visited[i]:
                stack.append()


# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end = ' ')


graph = [       #인접 리스트
    [],         #0번노드
    [2,3,8]     #1번노드
    [1,7]
    [1,4,5]
    [3,5]
    [3,4]
    [7]
    [2,6,8]
    [1,7]
]

visited = [False]*9

dfs_stack(graph, 1, visited)