def select(f, col):
    return [f(x) for x in col]
def where(f, col):
    return [x for x in col if f(x)]
data = '1 2 3 5 8 15 23 38'.split()
print(data)
res = select(int, data) # используем первую функцию int, которая преобразовывает строку в число
print(res)

res = where(lambda e: not e % 2, res)
res = list(select(lambda e: (e, e**2), res))
print(res)