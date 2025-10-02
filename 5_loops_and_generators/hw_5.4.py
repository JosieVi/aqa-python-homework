import array
from math import e
import numbers
import pytest

# TODO: 5.4 Примеры работы оператора цикла for. Функция enumerate

# Подвиг 1. На вход программе подается строка. Необходимо ее прочитать и найти в ней все индексы строкового фрагмента "ра". Выведите найденные индексы на экран в одну строчку через пробел. Если же фрагмент "ра" отсутствует в строке, то вывести -1.
# Sample Input:
# Барабанщик бил бой в барабан
# Sample Output:
# 2 23

# str = input("Input the phrase:").lower()
# flag = True
# for i in range(len(str)-1):
#     if str[i:i+2]  == "ра":
#         flag = False
#         print(i, end=' ')
# if flag:
#     print(-1)


# Подвиг 2. На вход программе подается строка с номером телефона. Ожидается следующий формат номера в строке:
# +7(xxx)xxx-xx-xx
# где x - это любая цифра. Число введенных символов считается верным (то есть, не может быть, чтобы отсутствовала какая-либо цифра или была лишняя). Необходимо прочитать строку из входного потока и проверить, что она содержит номер телефона в соответствии с приведенным форматом. Вывести "ДА", если это так и "НЕТ" в противном случае.
# Sample Input:
# +7(123)456-78-99
# Sample Output:
# ДА

# phoneNumber = input("Input phone number: ")
# numbers = "0123456789"
# flag = False
# if len(phoneNumber) < 16:
#     print("НЕТ")
# else:
#     for i, el in enumerate(phoneNumber):
#         if i == 0 and el != '+':
#             print("НЕТ")
#             break
#         elif i == 1 and el != '7':
#             print("НЕТ")
#             break
#         elif i == 2 and el != '(': 
#             print("НЕТ")
#             break
#         elif i in [3,4,5,7,8,9,11,12,14,15] and el not in numbers:
#             print("НЕТ")
#             break
#         elif i == 6 and el != ')':
#             print("НЕТ")
#             break       
#         elif i == 10 and el != '-':
#             print("НЕТ")
#             break      
#         elif i == 13 and el != '-':
#             print("НЕТ")
#             break
#     else:
#         flag = True
# if flag:
#     print("ДА")


# Большой подвиг 3. На вход программе подается строка, в которой записано арифметическое выражение. Например:
# "10 + 25 - 12"
# # или
# "10 + 25 - 12 + 20 - 1 + 3"
# и т. д. То есть, количество действий может быть произвольным.
# Необходимо прочитать эту строку из входного потока и выполнить вычисление, записанного в ней арифметического выражения. Результат вычисления отобразить на экране.
# Полагается, что в качестве арифметических операций используется только сложение (+) и вычитание (-), а в качестве операндов только целые числа. Следует учесть, что математические операции могут быть записаны как с пробелами (до и после), так и без них.
# P.S. В целях обучения программу следует делать без использования функции eval.
# Sample Input:
# 10+25 - 12
# Sample Output:
# 23

# expression = input()
expression = "-4 - 5 + 10"
expression = expression.replace(' ', '')
result = 0
expressionInArray = []

while expression:
    for i, el in enumerate(expression):
        if el in '+-' and i != 0:
            expressionInArray.append(expression[:i])
            expressionInArray.append(el)
            expression = expression[i+1:]
            break
    else:
        expressionInArray.append(expression)
        expression = ''

for i, el in enumerate(expressionInArray):
    if i == 0:
        result += int(el)

    elif el == '+':
        result += int(expressionInArray[i + 1])
    elif el == '-':
        result -= int(expressionInArray[i + 1])

print(result)


        

# Подвиг 4. На вход программе подаются целые числа, записанные в одну строку через пробел. Необходимо прочитать эти числа и сохранить в списке. Затем, каждое значение этого списка изменить на квадрат соответствующего числа. Результат (список) выведите на экран в виде последовательности чисел, записанных через пробел. Программу следует реализовать с использованием функции enumerate.
# Sample Input:
# 8 -11 4 3 6
# Sample Output:
# 64 121 16 9 36

# numbers = list(map(int, input().split()))
# for i, el in enumerate(numbers):
#     numbers[i] = el ** 2
# print(*numbers)


# Подвиг 5. На вход программе подаются целые числа, записанные в одну строку через пробел. Необходимо прочитать эти числа и сохранить в списке. Затем, каждый элемент этого списка продублировать один раз. Например, для списка:
# [1, 2, 3]
# после дублирования должны получить:
# [1, 1, 2, 2, 3, 3]
# Результат (список) выведите на экран в виде последовательности чисел, записанных через пробел.
# Sample Input:
# 8 11 2
# Sample Output:
# 8 8 11 11 2 2

# numbers = list(map(int, input().split()))
# doubleNumbers = []
# for el in numbers:
#     doubleNumbers.append(el)
#     doubleNumbers.append(el)    
# print(*doubleNumbers)


# Подвиг 6. На вход программе подаются вещественные числа, записанные через пробел. Необходимо прочитать эти числа и сохранить в списке. Затем, с помощью цикла for нужно найти наименьшее число в этом списке. Полученный результат (минимальное число) вывести на экран.  Реализовать программу без использования функции min, max и сортировки.
# Sample Input:
# 8.6 9.11 -4.567 -10.0 1.45
# Sample Output:
# -10.0

# floatNumbers = list(map(float, input().split()))
# minValue = floatNumbers[0]
# for el in floatNumbers:
#     if el < minValue:
#         minValue = el
# print(minValue)


# Подвиг 7. На вход программе подаются вещественные числа, записанные через пробел. Необходимо прочитать эти числа и сохранить в списке. Затем, все отрицательные значения в этом списке заменить на -1.0. Результат (список) выведите на экран в виде последовательности чисел, записанных через пробел. Программу следует реализовать с использованием функции enumerate.
# Sample Input:
# -5.67 3.5 6.89 -3.0
# Sample Output:
# -1.0 3.5 6.89 -1.0

# floatNumbers = list(map(float, input().split()))
# for i, el in enumerate(floatNumbers):
#     if el < 0:
#         floatNumbers[i] = -1.0
# print(*floatNumbers)