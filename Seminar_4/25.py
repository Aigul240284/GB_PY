# Задача №25

# Напишите программу, которая принимает на вход строку, и 
# отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split()
text_1='a a a b c a a d c d d'
#print(text_1)
# text_array=text_1.split()#строка остается, но потом убирается, остается список
# print(text_array)
import os
os.system('cls')
data={}
array=text_1.split()
#print(array)
res=''
for item in array:
    if item in data:
        data[item]+=1
        res += item+'_'+str(data[item])+' '
        print(data)
    else:
        data[item]=0
        res+=item+' '
        print(data)
#print(res)
    


    