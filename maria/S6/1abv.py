from random import sample
def l_r_w(count:int, alp:str='абв'):
    world_list=[]
    for i in range(count):
        letters=sample(alp, k=3)
     
        world_list.append("".join(letters))
  
    return " ".join(world_list)
def l_r_w_2(c:int, alp:str='абв'):
    return ' '.join(''.join(sample(alp,3)) for _ in range(c))
    
print (l_r_w(5))
print(l_r_w_2(5))


