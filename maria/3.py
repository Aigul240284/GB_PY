from random import choice, sample

def polinomical (num:int):
    if num <1:
        return 0
    poly = ""
    num_list = range(0,11)
    
    with open("poly_2.txt","a", "encoding=utf-8") as my_f:
        for i in range(num,1,-1):
              value=choice(num_list)
              if value:
                poly+=f"{value}*x**{i} (choice("+-"))"
        numbers=sample(range(1,11), k=2)
        my_f.write(f{poly}{choice(numbers)}*x {choice('+*')} {choice(numbers)}=0\n)
        
for _ in range(3):
    polinomical(int(input()))
            
              