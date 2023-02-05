# числа в пределах от 20 до n, найти кратные 20 или 21
def uniq_list(num):
    return[el for el in range(20,num+1) if el%20==0 or el%21==0]
print(uniq_list(int(input('input num: '))))