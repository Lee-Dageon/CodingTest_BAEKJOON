# 두 배열의 원소 교체
# 두 개의 배열 A와 B
# 두 배열은 N개의 원소 - 원소는 모두 자연수
# 최대 K번의 바꿔치기 연산
# A의 모든 원소의 합이 최대가 되도록 바꿔치기
# A와 B의 정보가 주어졌을 때
# 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는
# A의 모든 원소의 합의 최댓값

N, K = map(int, input(). split())
A = list(map(int, input(). split()))
B = list(map(int, input(). split()))

#A에 대해 오름차순 정렬
#B에 대해 내림차순 정렬

#A의 원소가 B의 원소보다 작을 때만 교체

A.sort()    #오름차순 정렬
B.sort(reverse = True)    #내림차순 정렬

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

print(sum(A))






