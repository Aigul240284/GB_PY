import math
# аргументы имена сотрудников, возвращает словарь, ключи первые буквы имен, 
# значения-списки создающие имена, начинабщие с соотв-щей буквы
from itertools import groupby
def thezaurus(*args):
    # print(*args)
    names_dict={}
    # print(names_dict)
    for i in sorted(args):
        # print(args)
        letter=i[0]
        if letter not in names_dict:
            names_dict[letter]=[i]
            # print(names_dict)
        else:
            names_dict[letter]+=[i]
            # print(names_dict)
    return names_dict
print(thezaurus('Иван','Мария','Петр','Илья','Дмитрий'))

def ts(*args):
    if '' not in args:
        return{ch:list(names)for ch, names in groupby(sorted(args), key=lambda i:i[0])}
    return 'Error'
print(ts('Иван','Мария','Петр','Илья','Дмитрий'))

def ts_3(*args):
    if '' not in args:
         return{ch[0]:list(filter(lambda el:el.startswith(ch[0]),args)) for ch in sorted(args)}
    return 'Error'  
print(ts_3('Иван','Мария','Петр','Илья','Дмитрий'))          