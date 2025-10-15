# TODO: 8.1 Импорт стандартных модулей. Команды import и from

# Подвиг 2. На вход программе подается вещественное число. Необходимо его прочитать, импортировать модуль math, вызывать функцию ceil модуля math для прочитанного числа и отобразить результат на экране.
# Sample Input:
# 5.67
# Sample Output:
# 6

from math import ceil
float_number = float(input())
print(ceil(float_number))


# Подвиг 3. На вход программе подается вещественное число. Необходимо его прочитать, импортировать только одну функцию floor из модуля math, вызывать ее для прочитанного числа и отобразить результат на экране.
# Sample Input:
# 8.11
# Sample Output:
# 8

from math import floor
float_number = float(input())
print(floor(float_number))


# Подвиг 4. В программе имеется функция factorial (см. листинг). В начале программы (до определения функции) необходимо из модуля math импортировать функцию с тем же именем factorial, используя команду from, но так, чтобы они не "затирали" друг друга. Имя импортируемой функции в модуле (программе) должно быть fact.

# Уже объявленную функцию не менять. Выполнять функции не нужно, только прописать импорт.

from math import factorial as fact

def factorial(n):
    p = 1
    for i in range(2, n+1):
        p *= i

    print("my factorial")
    return p


# Подвиг 5. Из модуля random импортируйте только две функции: seed и randint. Затем, в программе выполните их следующим образом:
# seed(1)
# print(randint(10, 50))

from random import seed, randint
seed(1)
print(randint(10, 50))


# Подвиг 6. Из модуля random импортируйте только две функции: seed и random, но у последней должен быть синоним rnd (имя, через которое она будет вызываться в программе). Выполните в программе эти функции, следующим образом:
# seed(10)
# print(round(rnd(), 2))

from random import seed, random as rnd
seed(10)
print(round(rnd(), 2))
