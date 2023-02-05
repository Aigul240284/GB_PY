from math import pi
import math
# def rounding(str):
#     if '.' in str:
#         return int(len(d)-d.find('.')-1)
#     else: return 0
    
# d= input('Введите точность числа n от 0.1 до 0.0000000001:  ')
# r = rounding(d)
# if 0.0000000001<=float(d)<=0.1:
#     print(f'Число пи с заданной точностью {d} = {round(pi,r)}')
# elif float(d)==0:
#     print(f'Число пи с заданной точностью {d} = {pi}')
# else:
#     print("Повторите ввод")
    
    
# print(len(str(3.123456789).split('.')[1]))


num_pi=str(math.pi)
d=len(input('input: 0.00: '))
print(d)
stop = num_pi.find('.')+d
print(stop)
print(num_pi[:stop])

print(round(math.pi, d))

    