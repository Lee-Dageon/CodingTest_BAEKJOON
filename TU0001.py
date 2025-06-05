# 주어진 정수와 그 정수를 reverse한 정수가 서로 같으면 회문
# N이 주어지고
# M이 소수이고 회문이 되는 가장 작은 정수 M을 찾는다.
# M >= N
# M이 소수이므로 M은 1과 M으로만 나누어 떨어져야 한다.
# N이 31이면 M은 101이다.

# Output
#
# 출력은 N보다 크거나 같은 가장 작고
# 소수 Palindrome을 만족하는 정수 M 출력

N = int(input())

# 소수 판정 함수 작성 -> M이 N보다 1씩 커지며 검사
# 소수라면 -> 회문 여부 검사

# 소수 판정 함수
def isPrime(N):
    if N < 2:
        return False
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            return False  # 소수 아님
    return True  # 소수 맞음

def isPalindrome(N):
    return str(N) == str(N)[::-1]


M = N
while True:
    if  isPalindrome(M) and isPrime(M):
        print(M, end='')
        break
    M += 1



                

                


