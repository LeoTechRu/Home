"""1 Задание. Код с использованием for:
Запросить целое число, после чего вывести на экран все числа от 0 до введенного числа включительно через цикл for.
Функция range(n + 1) возвращает последовательность чисел от 0 до n включительно. Значение i поочередно принимает
каждое из чисел этой последовательности, и для каждого из них выполняется команда print(i)."""
for i in range(int(input()) + 1):
    print(i)
"""2.Программа делает то же самое, что и предыдущая, но использует цикл while вместо цикла for."""
a = int(input())
i = 0
while i < a:
    i += 1
    print(i)
