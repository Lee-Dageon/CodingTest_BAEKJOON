# 다트 문제

def solution(dartResult):
    answer = 0      #최종점수
    score = 0      #현재 기회의 점수
    current = 0     #현재 기회의 계산된 점수
    previous = 0    #이전 기회의 계산된 점수

    for c in dartResult:        # 문자 하나씩 검사
        if '0'<=c<='9': # 점수는 0점~10점
            if c == '0' and score == 1:
                score = 10
            else:
                score = int(c)
        elif c == 'S':
            previous = current
            current = score ** 1
            answer += current
        elif c == 'D':
            previous = current
            current = score ** 2
            answer += current
            pass
        elif c == 'T':
            previous = current
            current = score ** 3
            answer += current
            pass
        elif c == '*':
            answer -= (previous + current)
            previous *= 2
            current *= 2
            answer += (previous + current)
            pass
        elif c == '#':
            answer -= current
            current *= -1
            answer += current

    return answer

# 함수 만들기

# 문자열 입력받기(문자 하나하나 판단)
# S이면 바로 전숫자 ^1, R이면 바로 전숫자^2, T이면  바로 전숫자^3
# 결과 출력





