from random import randrange

def list_rand_nums(count:int):
    if count<0:
        print('Negative value of the number of numbers!')
        return[]
    list_nums=[]
    for i  in range(count):
        list_nums.append(randrange(count))
    return list_nums
    
list_num= list_rand_nums(10)
print(list_num)



def uniq_el(list_nums:list):
    result=[]
    my_dict={}.fromkeys(list_nums,0)
    
    for i in list_nums:
        my_dict[i]=+1
    print(my_dict)
        
    for k in my_dict:
        # if my_dict[k]==1:
        result.append(k)
    
    return result

print(uniq_el(list_num))
            
        
        