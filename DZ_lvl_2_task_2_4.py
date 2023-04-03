# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

s = input('Введите Вашу строку: ')

def remove_exclamation_marks(s):
    result_str = ''
    for i in range(len(s)):
        if s[i] != '!':
            result_str += s[i]
    return result_str
print(remove_exclamation_marks(s))