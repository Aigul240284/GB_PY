# Задача №17 

# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
import random
n = int(input('Введите длину списка: '))


list_1=[]
for _ in range(n):
    list_1.append(random.randint(-10, 10))
list_1.sort()      
print(list_1)
my_set=set(list_1)
# my_list2 = list(my_set)
print(len(my_set))




