# Задача 10 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2
import random
def mones(N):
    heads_tails=[]
    for _ in range(num_coins):
        heads_tails.append(random.randint(0, 1))
    print(heads_tails)
    tails=heads=0
    for item in heads_tails:
        if item == 0:
            tails+=1
        else: 
            heads+=1
    if tails < heads:
        return(f'You can flip {tails} coins')
    else: return(f'You can flip {heads} coins')
try:
    num_coins = int(input('TASK №10: Input the number of coins: '))    
    print(mones(num_coins))
except:
    print(f'Iinvailid input, please, try again.')

# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.



try:
    sum = int(input('TASK №12: Input the sum of the hidden numders: '))
    product = int(input('Input the product of the hidden numders: '))
    task_answer=0
    for i in range(sum):
        if i*(sum-i)==product:
            print(f'Petya quessed the numbers: {i} and {sum-i}')
            task_answer=1
            break
    if task_answer==0:
        print('These numbers are wrong, please, try again.')
        
except:
    print('Invailid input, please, try again.')
    
# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2 в степени k), не превосходящие числа N
num = int(input('TASK №14: Input the number: ')) 
s=num*0.5
list_1 = [i * i for i in range(1,s) if i%2==0 and i < num]
# print(list_1) 
# list_1 = list() # создание пустого списка

# for i in range(num): # цикл выполнится 5 раз
#     n = 1
#     n*=2
#     list_1.append(n)
print(list_1) 