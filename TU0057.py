# 모든 순열을 출력

# N, K
# N개의 순열을 포함하는 K줄

N, K = map(int, input.split())

# 다음 순열 출력
for _ in range(K):                       # K개 순열 반복 #2
    L = list(map,(int, input().split())) # L = [1, 3, 4, 2]

    for i in range(N-1, 0, -1):
        if L[i-1] < L[i]:
            R = L[i-1:]
            R.sort()
            j = R.index(L[i-1])
            number =  R.pop(j+1)
            R.insert(0, number)
            L = L[:i-1] + R
            break

    for n in L:
        print(n, end=' ')
    print()                             # 한 줄 띈다.



