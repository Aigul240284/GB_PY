# def calc1(x):
#     return x*x
# def calc2(x):
#     return x+x

def math(z,x,y):
    print(z(x,y))

calc1=lambda a,b: a+b
    
math(calc1,5,45)
math(lambda a,b: a+b,5,45)