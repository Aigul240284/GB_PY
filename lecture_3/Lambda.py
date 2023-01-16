# def calc2(x):
#     return x*10

# def math (op,x):
#     print(op(x))
    
# math(calc2, 10)

# # def sum(x,y):
# #     return x+y
# # f=sum
# f=lambda q,w:q+w #!!!!!!!!!!!!!!!!!!!

# def mult(x,y):
#     return x*y
# def calc (op,a,b):
#     print((op(a,b)))
#     return op(a,b)
# calc(mult, 4, 5)
# calc(f, 4, 5)

# calc(lambda q,w:q+w, 4, 5)

path ='/Users//компьютер/Desktop/обучение/file.txt'
f = open(path,'r')
data = f.read() + ' '
print(data)
f.close()

numbers = []

while data != '':
    space_pos=data.index(' ')
    numbers.append(int(data[:space_pos]))
    data=data[space_pos+1:]
    # print(space_pos)
print(numbers)

out = []
for e in numbers:
    if not e % 2:
     out.append((e,e **2))
print(out)