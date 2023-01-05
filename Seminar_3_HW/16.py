import random
import os
os.system('cls')
# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.
# Ввод: 5
# Ввод: 1
# 1 2 1 2 2
# Вывод: 2
lenght_array = int(input('DZ№ 16 \n Введите длину списка: '))
list_1 = []
for _ in range(lenght_array):
    list_1.append(random.randint(1, lenght_array//2))
print(list_1)
num = int(input('Введите число, которое нужно найти в массиве: '))
count = 0
for i in range(0, lenght_array):
    if list_1[i] == num:
        count += 1
print(count)



# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6
print('DZ18')
os.system('cls')
lenght_array = int(input('DZ№ 18 \n Введите длину массива: '))
list_1 = []
for _ in range(lenght_array):
    list_1.append(random.randint(1, lenght_array//2))
print(list_1)
num = int(input('Введите число, которое нужно найти в массиве: '))
find_num = 0
count==0
for i in range(0, lenght_array):
    dif_num=list_1[i] - find_num
    if dif_num<count:
       count=dif_num
       find_num=list_1[i] 
print(find_num)
