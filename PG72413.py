#플로이드-와샬 알고리즘


INF = int(1e9)

def Floyd_Warshall(n,fares):
    d = [ [INF] * (n+1 for _ in range(n+1))]
    for i in range(1, n+1)
        d[i][i] = 0

    for u,v,w in fares: #u<->v 최단거리 w로 설정
        d[u][v] = w
        d[v][u] = w

    # 점화식 Dab = min(Dab, Dak + Dkb)
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                d[a][b] = min(d[a][b], d[a][k] + d[k][b])




def solution(n,s,a,b,fares):
    d = Floyd_Warshall()
    answer = 0
    return answer




