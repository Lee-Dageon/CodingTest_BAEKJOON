# 숫자 두개 입력받고
# 문자열 입력받기
#첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다.
# 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과,
# N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다.
# 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며,
# 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.

#듣도 못한 사람의 명단에는 중복되는 이름이 없으며,
# 보도 못한 사람의 명단도 마찬가지이다.

#python 의 input은 문자열을 받는다. (int로 받을 수 없음)
N, M = map(int,input().split())
D = set()
for _ in range(N): # 듣도 못한 사람 집합
    D.add(input())

B = set()
for _ in range(M): # 보도 못한 사람 집합
    B.add(input())

DB = list(D&B)  #교집합 듣보잡
DB.sort()     #사전순으로 정렬
print(len(DB))

for p in DB:
    print(p)

