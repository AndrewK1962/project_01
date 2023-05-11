# Задача 2.4. Пункт B.
# Напишите функцию, которая  удаляет восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

# def remove_last_em(s):
#     pass


def remove_exclamation_mark(input_string):
    if input_string.endswith('!'): 
    # endswith проверяет, заканчивается ли строка на заданный символ или подстроку
        input_string = input_string[:-1] 
        # если да, то удаляем последний символ
    return input_string

# Например:
input_string = input("Введите строку: ")
new_string = remove_exclamation_mark(input_string)

print(new_string)


# Результат:

# Введите строку: Hello World!
# Hello World
