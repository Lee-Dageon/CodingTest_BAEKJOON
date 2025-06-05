# 장르별로 가장 많이 재생된 노래를 두 개씩 모아
# 베스트 앨범 출시
# 속한 노래가 많이 재생된 장르를 먼저 수록
# 장르 내에서 많이 재생된 노래를 수록
# 같은 장르, 같은 재생 횟수 -> 고유 번호 낮은 것부터

# genres, plays,

genres = input()
genres_input = genres.strip("[]").replace('"', '').replace(",", " ")
genres = genres_input.split()

plays = input()
plays_input = plays.strip("[]").replace('"', '').replace(",", " ")
plays = plays_input.split()
# play를 int로 바꾸기
plays = list(map(int, plays))

# 고유 번호 리턴
def solution(genres, plays):

    # 입력 데이터
    # ["classic", "pop", "classic", "classic", "pop"]
    # [500, 600, 150, 800, 2500]

    # 고유번호 붙이기
    # [(0, 'classic', 500), (1, 'pop', 600), ...]
    songs = []
    for i in range(len(genres)):
        songs.append((i, genres[i], plays[i]))

    # 1. 장르별 재생 횟수 합산
    # 딕셔너리 이용 {key:value}
    genres_play_count = {}
    for song in songs:  #모든 곡을 돌면서
        genre = song[1]
        play = song[2]

        if genre in genres_play_count:
            genres_play_count[genre] += play
        else:
            genres_play_count[genre] = play

    #{'classic': 1450, 'pop': 3100}
    #print(genres_play_count)

    #2. 재생 횟수가 많은 장르부터 차례대로 sort하기
    sorted_genres = sorted(genres_play_count,   #key값만 뽑아서 sort
                           key=lambda x: genres_play_count[x],  #value값 기준으로 정렬
                           reverse=True)

    # print(sorted_genres)
    # ['pop', 'classic']

    #3. 각 장르에서 노래 뽑기
    answer = []     #리스트

    #장르별로 노래 모으기
    for genre in sorted_genres:    #장르마다
        genre_songs = []            #각각의 리스트로 저장됨
        for song in songs:      #노래 하나씩 검사하면서
            if song[1] == genre:    #노래가 그 장르이면
                genre_songs.append(song)


    # [(1, 'pop', 600), (4, 'pop', 2500)]
    # [(0, 'classic', 500), (2, 'classic', 150), (3, 'classic', 800)]

    # 각 장르마다 재생 횟수가 많은 순서대로 정렬
    # 재생 횟수 같으면 고유번호 낮은 것부터
        genre_songs.sort(key=lambda x:(-x[2], x[0]))

        # 노래 2개씩만 담기
        count = 0
        for song in genre_songs:
            answer.append(song[0])      #고유 번호만 저장
            count += 1
            if count == 2:
                break

    return(answer)



# result = solution(genres, plays)
# print(result)








