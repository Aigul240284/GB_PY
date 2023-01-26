def power(base, exp):
    if (exp == 1):
        return (base)
    if (exp != 1):
        return (base * power(base, exp - 1))
base = int(input("Введите число: "))
exp = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", power(base, exp))

def sum (a, b):
    if (a==1 or b==1):
        return (a+b)
    else:
        return (sum(a+1,b - 1))
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print("Результат суммы равен:", sum(a, b))


