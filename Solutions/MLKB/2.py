num = int(input('Введите целое число: '))  # запросили целое число
if num % 2 == 0:  # Если при делении на 2 остаток 0, то
    print('Данное число четное')  # Выводим, что число чётное
else:  # Иначе
    print('Данное число не является четным')  # Выводим, что число нечетное

num1 = float(input('Введите первое число: '))  # Запросили ввод вещественного числа, т.к. в ТЗ нет про целочисленные
num2 = float(input('Введите второе число: '))  # Запросили ввод второго вещественного числа, т.к. в ТЗ нет про целочисленные
if num1 > num2:  # Если первое больше, значит его и выводим
    print(num1)
elif num1 < num2:  # Если первое меньше, выводим второе
    print(num2)
else:  # А если они равны, то мы выводим песню Антошки, т.к. этого нет в ТЗ. Если этого не сделать - будет пустой ответ.
    print('Это мы не проходили, это нам не задавали\nТили-тили, трали-вали'
          '\nЭто мы не проходили, это нам не задавали\nПа-рам-пам-пам, Па-рам-пам-пам')

n1 = int(input('Введите номер столбца: '))  # Запросили ввод целого числа, т.к. в шахматах не будет вещественных нумераций полей)
n2 = int(input('Введите номер ряда: '))  # Запросили ввод второго целого числа
if (n1+n2)%2 == 0: # Если сумма номеров столбца и ряда четная, значит клетка чёрная
    print('NO') #Выводим NO как и просили в ТЗ
elif (n1+n2)%2!=0: #Если сумма номеров столбца и ряда нечётная, значит клетка белая
    print('YES') #Выводим YES
else: #Иначе всегда должно быть на случай сбоя матрицы)
    print('Срочно вызывайте агента Смита! Произошёл сбой матрицы!')
