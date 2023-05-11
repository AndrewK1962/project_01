# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

# def switch_it_up(number):
#     pass
def switch_it_up(number):
    digits_dict = {
        0: 'ноль',
        1: 'один',
        2: 'два',
        3: 'три',
        4: 'четыре',
        5: 'пять',
        6: 'шесть',
        7: 'семь',
        8: 'восемь',
        9: 'девять'
    }

    return digits_dict.get(number, 'Такой цифры нет, это уже число')

# Например:
number = int(input("Введите цифру от 0 до 9: "))

# цифра прописью
number_in_words = switch_it_up(number)

print(number_in_words)

# Результат:

# Введите цифру от 0 до 9: 7
# семь

# Введите цифру от 0 до 9: 22
# Такой цифры нет, это уже число