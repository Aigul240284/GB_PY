from random import sample
from random import randint

def more_then(num):
    my_list=sample(range(num*3), num)
    print(my_list)
    return [my_list[num] for num in range(1,len(my_list)) if my_list[num]>my_list[num-1]]
   
print(more_then(int(input('input num: ')))) 

def more(num):
    lt=[randint(0, 1000) for _ in range(num)]
    print(lt)
    return[elem for i, elem in enumerate(lt[1:]) if elem>lt[i]]
print(more(int(input('input num: ')))) 
    