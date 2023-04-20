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

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    result_str = ''
    if s[-1] == '!':
        result_str += s[0:-1]
        return result_str
    else:
        return s

print(remove_last_em(s))


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"


def remove_word_with_one_em(s):
    result_str = ''
    k = 0
    splitted_line = s.split(' ')
    length = len(splitted_line)
    for i in range(length):
        j = len(splitted_line[i])
        l = splitted_line[i]
        for i in range(j):
            o = l[i]
            if ord(o) == 33:
                k += 1
        if k == 1:
            result_str += ''
        else:
            result_str += (l + ' ')
        k = 0
    return result_str

print(remove_word_with_one_em(s))

# Ох, последний я вот покороче записал
def remove_word_with_one_em(s):
    return ' '.join([w for w in s.split(' ') if w.count('!')!=1])

print(remove_word_with_one_em("Hi! Hi!! Hi!"))
