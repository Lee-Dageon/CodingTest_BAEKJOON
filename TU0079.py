#문자열 두 세트를 입력받고,
#문자열을 비교하여 같으면 공백으로 대체 s.replace() 함수
#다시 비교
#이전 문자열과 이후 문자열이 같은 부분이 없을 때까지
#계속 없앤다.


orig = input()
bomb = input()

# 계속 반복하면서 bomb을 제거
while bomb in orig:
    orig = orig.replace(bomb, "")

# 결과 출력
print(orig)






