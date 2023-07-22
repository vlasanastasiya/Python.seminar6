#Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате 
# DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года — 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
from datetime import datetime
# from sys import argv


def validation_date(year: str) -> bool:
    return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)


def val_date(txt: str) -> bool:
    try:
        value = datetime.strptime(txt, "%d.%m.%Y").date()
        return True
    except:
        return False
    
# if __name__ == '__main__':
#     print(val_date('34.06.2023'))

# if __name__ == '__main__':
#     if len(argv) != 2:
#         print("Должна быть дата в формате ДД.ММ.ГГ")
#     else:
#         input_date = argv[1]
#         if val_date(input_date):
#             print("Такая дата есть")
#         else: print("Такой даты нет")


# ----------------------------------------------------------------
# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 
# ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, 
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# 4. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в 
# задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
import itertools
import random

def attacking(position_of_queens):
    for i in range(len(position_of_queens)):
        for j in range(i + 1, len(position_of_queens)):
            row_1, column_1 = position_of_queens[i]
            row_2, column_2 = position_of_queens[j]

            if row_1 == row_2 or column_1 == column_2 or  abs(row_1 - row_2) == abs(column_1 - column_2):
                return False
    return True

def generation():
    list_of_placement = []
    all_permutations = list(itertools.permutations(range(1, 9)))
    random.shuffle(all_permutations)

    for permutation in all_permutations:
        position_of_queens = [(i + 1, permutation[i]) for i in range(8)]

        if attacking(position_of_queens):
            list_of_placement.append(position_of_queens)

            if len(list_of_placement) == 4:
                break
    return list_of_placement

list_of_placement = generation()

print("Расстановка фрезей")
for i, arrangement in enumerate(list_of_placement, 1):
    print(f"Расстановка {i}: {arrangement}")


