# Задача 1.1.

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

song1 = my_favorite_songs[:14]
song2 = my_favorite_songs[16:30]
song3 = my_favorite_songs[33:50]
song4 = my_favorite_songs[51:62]
song5 = my_favorite_songs[64:]

print(song1)
print(song5)
print(song2)
print(song4)

# Чтобы не считать индексы вручную можно воспользоваться следующими методами
# Решение с помощью индексации строк

first_song = my_favorite_songs [
    : my_favorite_songs.find(',')
]

last_song = my_favorite_songs [
    my_favorite_songs.rfind('N') :
]

second_song = my_favorite_songs[
     my_favorite_songs.find('S') : 
     my_favorite_songs.find(', A')
]

previous_song = my_favorite_songs [
    my_favorite_songs.rfind('St') : 
    my_favorite_songs.rfind(', N')
    ]

print(first_song, last_song, second_song, previous_song)


# Решение с помощью метода split() и индексации списков
songs = my_favorite_songs.split(', ')

print(songs[0], songs[-1], songs[1], songs[-2])
