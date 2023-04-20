# Задача 1.2.
# Пункт А.

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

time = 0
print(my_favorite_songs)
print("Выберите три песни из списка от 0 до 8:")
num = int(input())
time += my_favorite_songs[num][1]
num = int(input())
time += my_favorite_songs[num][1]
num = int(input())
time += my_favorite_songs[num][1]
print("Три песни звучат ", time, " минут")

# Выполнено
