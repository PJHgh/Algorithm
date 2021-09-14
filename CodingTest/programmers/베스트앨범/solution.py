def solution(genres, plays):
    genre2plays = {}
    genre2total_plays = {}
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre in genre2plays.keys():
            genre2plays[genre].append((play, i))
            genre2total_plays[genre] += play
        else:
            genre2plays[genre] = [(play, i)]
            genre2total_plays[genre] = play
    genres_order = list(map(lambda x:x[0], sorted(genre2total_plays.items(), key=lambda x:x[1], reverse=True)))
    
    answer = []
    for genre in genres_order:
        playlists = genre2plays[genre]
        playlists = list(map(lambda x:x[1], sorted(playlists, key=lambda x:x[0], reverse=True)))
        answer.extend(playlists[:2])
    return answer