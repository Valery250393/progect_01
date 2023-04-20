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
print('min =', res_min, 'max =', res_max)

# Супер!)
# Вот вариант с быстрой сортировкой
def quicksort(arr):
    if len(arr) < 2:
        # базовый случай, массив с 0 или 1 элементом уже отсортирован
        return arr
    else:
        # рекурсивный случай. выберем опорный элемент pivot
        pivot = arr[0]
        # подмассив всех элементов, меньших, чем опорный элемент pivot
        less = [i for i in arr[1:] if i <= pivot]
        # подмассив всех элементов, превышающих опорный элемент pivot
        greater = [i for i in arr[1:] if i > pivot]
        # обединяем в порядке "сортировка для меньшего подмассива – опорный элемент – сортировка для большего подмассив"
        return quicksort(less) + [pivot] + quicksort(greater)

# Максимум - это последний элемент отсортированного списка
def maximum(arr):
    return quicksort(arr)[-1]

 # Минимум - это первый элемент отсортированного списка
def minimum(arr):
    return quicksort(arr)[0]
print('\nБыстрая сортировка')
print('min =', minimum([4,6,2,1,9,63,-134,566]))
print('max =', maximum([4,6,2,1,9,63,-134,566]))
