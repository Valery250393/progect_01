# Задача 1.2.
# Пункт B.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

time = 0
print(my_favorite_songs_dict)
print("Введите название трех песен из списка:")
num = str(input())
time += my_favorite_songs_dict[num]
num = str(input())
time += my_favorite_songs_dict[num]
num = str(input())
time += my_favorite_songs_dict[num]
print("Три песни звучат ", round(time, 2), " минут")

# Выполнено
