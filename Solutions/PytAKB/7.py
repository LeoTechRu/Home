"""Задание 1: Операции с кортежами
Условие: Создайте кортеж, содержащий три целых числа. Выведите на экран каждое число, а затем выведите их сумму.
Пример вывода:
Кортеж: (2, 4, 6)
Первое число: 2
Второе число: 4
Третье число: 6
Сумма: 12"""
a = (2, 4, 6)  # кортеж
print(a[0], a[1], a[2], sep='\n')  # вывод кортежа по частям

"""2. Работа со списками и множествами
Вводятся два списка чисел. Выведите, сколько чисел содержится одновременно в двух списках.
Пример вывода:
Введите первый список: 1 2 6 7
Введите второй список: 2 7 5 9
Количество пересечений: 2"""
it = 0  # итератор для подсчёта вхождений
for i in [1, 2, 6, 7] :  # берём элемент из первого списка
    if i in [2, 7, 5, 9] :  # если элемент есть во втором списке
        it += 1  # добавляем +1 к итератору
    else:  # иначе
        continue  # пропустить
print(it)  # выводим количество пересечений
