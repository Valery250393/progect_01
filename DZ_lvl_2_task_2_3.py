# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

number = int(input('Введите значение от 0 до 9: '))

def switch_it_up(number):
    while 0 <= number <= 9:
        return f'Вы ввели {number} -> {number_in_words[number]}'
    return f'Вы ввели {number} -> None'
number_in_words = [
    'Zero',
    'One',
    'Two',
    'Three',
    'Four',
    'Five',
    'Six',
    'Seven',
    'Eight',
    'Nine'
]

print(switch_it_up(number))