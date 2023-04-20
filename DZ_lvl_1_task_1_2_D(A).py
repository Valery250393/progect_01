# Задача 1.2.
# Пункт D (для пункта A).

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

from datetime import time
from random import randint
time1 = 0
print(my_favorite_songs)
num = randint(0, 8)
time1 += my_favorite_songs[num][1]
print(num)
num = randint(0, 8)
time1 += my_favorite_songs[num][1]
print(num)
num = randint(0, 8)
time1 += my_favorite_songs[num][1]
print(num)

datetame.time(time1)
print("Три случайные песни звучат ", datetame.time(time1), " минут")

# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

# Забыл про время. Вот мой вариант
from random import sample
from datetime import timedelta
from math import modf

time = 0
for song in sample(tuple(my_favorite_songs_dict), 3):
    time += my_favorite_songs_dict[song]

print(f'Пункт C(B): Три песни звучат {round(time, 2)}')
