# Задача 2.4. Пункт A.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строки.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

# def remove_exclamation_marks(s):
#     pass

def remove_exclamation_marks(input_string):
    output_string = input_string.replace('!', '') 
    # replace удаляет все вхождения заданного символа из строки
    return output_string

# Например:
input_string = input("Введите строку: ")
new_string = remove_exclamation_marks(input_string)

print(new_string)


# Результат:

# Введите строку: Hello World!
# Hello World