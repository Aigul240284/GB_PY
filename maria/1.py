from random import choice, sample

def make_list():
    num= int(input("Input your number, please: "))
    ls=[i for i in range(num+1)]
    ls.remove(choice(ls))
    print(ls)
    return ls
   

def find_num(lst):
    for i in range(1,len(lst)):
        if lst[i]-1!=lst[i-1]:
            return lst[i]-1
 
print(find_num(make_list()))
