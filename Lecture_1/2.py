# Типы данных:
# int, float, boolean, str, list, None
value = None
value = 1234
print(type(value))
s="hello"
print(type(s))
a = 14
b = 'hi'
print(a,b,s)
print(a, '-', b, '-', s)
print('{} - {} - {}'.format(a,b,s))
print(f'{a} - {b} - {s}')
print('{1} - {2} - {0}'.format(a,b,s))
# a=input('input a')
# b=input('input b')
# print(a+b)
# a=int(input('input a'))
# b=int(input('input b'))
# print(a+b)
# Если помните математику – проблем не будет
# +, -, *, /, %, //, **
# Приоритет операций **, ⊕, ⊖, *, /, //, %, +, -
# ( ) Скобки меняют приоритет
print('целочисленное деление', 12//5) # целочисленное деление
print('возведение в степень',2**2) # возведение в степень
print('округление по правилам математики',round(2*1.3))
print('округление до 2х чисел после запятой',round(2*1.3,2))

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not i
print('верно хотябы одно - or', 1>2 or 4<6) # верно хотябы одно 
f=[1,2,3,4]
print(f)
print('2 в списке', 2 in f)
print('2х нет в списке', not 2 in f)
is_odd = f[0]%2==0
print(is_odd)
is_odd = not f[0]%2
print(is_odd)
#elif
original=456
inverted=0
while original!=0:
    inverted=inverted*10+(original%10)
    original//=10
    print(inverted,original)
else:
    print('Пожалуй, хватит!')
print(inverted)

#for
for i in 1,2,3,4,5:
    print(i**2)
print('\n')
r=range(5)
for i in r:
    print(i)
print('\n')  
for i in range(1,5,2):
    print (i) 
print('\n')  
    #Немного о строках
text = 'съешь ещё этих мягких французских булок'
print(len(text)) # 39
print('есть ли в тексте слово еще?', 'ещё' in text) # True 
print('являются ли все символы числами', text.isdigit()) # False
print('являются ли все символы логическим выражением', text.islower()) # True
print(text.replace('ещё','ЕЩЁ')) 
for c in text:
    print(c)
text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...

ran = range(1,6)
print(type(ran))
numbers = list(ran)
print(type(numbers))
print(len(numbers))
print(numbers)

for i in numbers:
    i*=2
    print(i)
print(numbers)

colors = ['red', 'green', 'blue']

print(colors)
for e in colors:
    print(e)
print(colors)

for e in colors:
    print(e*2)

colors.append('gray')
print(colors) 
colors.remove('blue') 
print(colors) 
del colors[0] 
print(colors) 

def f(x):
    if x == 1:
        return 'Целое'
    if x == 2.3:
        return 23
    else: return
arg = 're'
print(f(arg))
print(type(f(arg)))    