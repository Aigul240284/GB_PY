# список, описывающий возрастающую последовательность

from random import choices

def fill_list():
    n= int(input("input the lenght of the list: "))
    my_list = choices(range(n*2), k=n )
    # print(my_list)
    return my_list

def sort_list(s_list):
    new_list=[]
    for i in range(len(s_list)):
        temp=s_list[i]
        d_list=[temp]
        for j in range(i+1, len(s_list)):
            if s_list[j]>temp:
                temp=s_list[j]
                d_list.append(temp)
        if len(d_list)>1:
            new_list.append(d_list)
    # print(new_list)
    return new_list

a=fill_list()
print(a)
print(sort_list(a))
        
    



    
    