# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# data = open('tel.txt', 'r+')
# data.writelines('hello world'+ "\n")

# print(data.readline())
# data.close()

file_Name='tel.txt'

def WriteFile(file_name):
    with open(file_name, 'a') as data:
        data.writelines('hello world22' + '\n')
        
def ReadFile(file_name):
    result=[]
    with open(file_name, 'r+') as data:
        for line in data:
            result.append(line.split())
    return result

# def findUser(user_list):
#     name= 'Ivan,'
#     for user in user_list:
#         # print(user)
#         if user[1]==name:
#             print(user[3])
            
def deleteUser(user_list):
    name= 'Ivan,'
    for user in user_list:
        # print(user)
        if user[1]==name:
           remove(user)
        print(user_list)

# def deleteUser(user_list):
#         name= 'Ivan,'
#         for line in user_list:
#             print(line)
#             # if name == line:
#             #     people.remove(name)

 
        
# WriteFile(file_Name)
# print(type(ReadFile(file_Name)))
# print(ReadFile(file_Name))
# findUser(ReadFile(file_Name))
deleteUser(ReadFile(file_Name))
    
