<<<<<<< HEAD
# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции max и min использовать нельзя!


def minimum(arr):
    min_number = arr[0]
    for num in arr:
      if num < min_number:
        min_number = num
    return min_number

def maximum(arr):
    max_number = arr[0]
    for number in arr:
      if number > max_number:
        max_number = number
    return max_number

lst1 = [4, 6, 2, 1, 9, 63, -134, 566]
#lst1 = [-52, 56, 30, 29, -54, 0, -110]
#lst1 = [42, 54, 65, 87, 0]
#lst1 = [5]

res_min = minimum(lst1)
res_max = maximum(lst1)
=======
# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции max и min использовать нельзя!


def minimum(arr):
    min_number = arr[0]
    for num in arr:
      if num < min_number:
        min_number = num
    return min_number

def maximum(arr):
    max_number = arr[0]
    for number in arr:
      if number > max_number:
        max_number = number
    return max_number

lst1 = [4, 6, 2, 1, 9, 63, -134, 566]
#lst1 = [-52, 56, 30, 29, -54, 0, -110]
#lst1 = [42, 54, 65, 87, 0]
#lst1 = [5]

res_min = minimum(lst1)
res_max = maximum(lst1)
>>>>>>> f916a8d59fab60c24abeacf2d1f29bcdf668f574
print('min =', res_min, 'max =', res_max)