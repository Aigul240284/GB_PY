from random import randint
    
count_candys=(201)    
print(f'Всего конфет: {count_candys}')
def game(sweets:int):
    while sweets>0:
        while sweets>=28:
            boots_player = int(sweets%29)
            print(f"компьютер взял {boots_player} штук")
            # if sweets!=0: 
            #     boots_player = int(sweets%28+1)
            #     print(f"компьютер взял {boots_player} штук")
            #     sweets-=boots_player
            # else: boots_player==28
            sweets-=boots_player
            print(f'осталось конфет: {sweets}')
            candy_player = int(input('Возьми не более 28 конфет:  '))
            sweets-=candy_player
            print(f'осталось конфет: {sweets}')
        else: boots_player = int(sweets)
        print(f'компьютер победил, забрал последние конфеты')
        break
    
        
        
game(count_candys)
    
    
        
        
    
    