# Задача 1.2.
# Пункт С (для пункта А).

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

from random import randint
time = 0
print(my_favorite_songs)
num = randint(0, 8)
time += my_favorite_songs[num][1]
print(num)
num = randint(0, 8)
time += my_favorite_songs[num][1]
print(num)
num = randint(0, 8)
time += my_favorite_songs[num][1]
print(num)
print("Три случайные песни звучат ", round(time, 2), " минут")

# Можно все-таки записать это несколько покороче
# Пункт С(А)
from random import sample

time = 0
for song in sample(my_favorite_songs, 3):
    time += song[1]

print(f'Пункт C(A): Три песни звучат {round(time, 2)}')
