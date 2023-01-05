# Задача №19

# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  K – положительное число.

# Input:   [1, 2, 3, 4, 5] k = 2
# Output:  [4, 5, 1, 2, 3]
import os
os.system('cls')
import random
n = int(input('Введите длину списка: '))
list_1=[]
for _ in range(n):
    list_1.append(random.randint(-10, 10))     
print(list_1)
k = int(input('Введите на сколько индексов сдвигать? '))
for _ in range(k):
    p=list_1.pop(-1)
    list_1.insert(0,p)
print(list_1)