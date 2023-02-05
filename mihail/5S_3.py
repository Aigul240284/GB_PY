my_str="Абв ыва 12 jhj, кабвпв ыук абв йцк фв в аБв"
# my_str= my_str.lower().split()
print(my_str)

new_str=' '.join(list(filter(lambda elem: 'абв' not in elem.lower(), my_str.split())))
print(new_str)
    
