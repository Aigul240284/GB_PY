# Задача №23

# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает 
# количество элементов массива, больших предыдущего 
# (элемента с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2
import os
os.system('cls')
import random
n = int(input('Введите длину списка: '))
list_1=[]
for _ in range(n):
    list_1.append(random.randint(0, 10))
print(list_1)
count=0
for _ in range(1,len(list_1)):
    if list_1[_-1]<list_1[_]:
        count+=1
print(count)