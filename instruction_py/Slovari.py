# Словарь (dictionary) в языке Python хранит коллекцию элементов, 
# где каждый элемент имеет уникальный ключ и ассоциированое с ним 
# некоторое значение.

dictionary = { ключ1:значение1, ключ2:значение2, ....}
users = {1: "Tom", 2: "Bob", 3: "Bill"}

emails = {"tom@gmail.com": "Tom", "bob@gmai.com": "Bob", "sam@gmail.com": "Sam"}

objects = {1: "Tom", "2": True, 3: 100.6} #Но необязательно ключи и строки должны быть однотипными.

#### Пустой словарь без элементов
objects = {}
objects = dict()

# Преобразование списков и кортежей в словарь

users_list = [
    ["+111123455", "Tom"],
    ["+384767557", "Bob"],
    ["+958758767", "Alice"]
]
users_dict = dict(users_list)
print(users_dict)      # {"+111123455": "Tom", "+384767557": "Bob", "+958758767": "Alice"}


users_tuple = (
    ("+111123455", "Tom"),
    ("+384767557", "Bob"),
    ("+958758767", "Alice")
)
users_dict = dict(users_tuple)
print(users_dict)

###### Получение и изменение элементов

dictionary[ключ]

users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
 
# получаем элемент с ключом "+11111111"
print(users["+11111111"])      # Tom
 
# установка значения элемента с ключом "+33333333"
users["+33333333"] = "Bob Smith"
print(users["+33333333"])   # Bob Smith

users["+4444444"] = "Sam" #добавление ключа с элементом
user = users["+4444444"]    # KeyError - если в словаре нет, то выйдет ошибка

key = "+4444444" # Проверка наличия ключа
if key in users:
    user = users[key]
    print(user)
else:
    print("Элемент не найден")
    
# get(key): возвращает из словаря элемент с ключом key. Если элемента с таким ключом нет, то возвращает значение None

# get(key, default): возвращает из словаря элемент с ключом key. Если элемента с таким ключом нет, то возвращает значение по умолчанию default
users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
 
user1 = users.get("+55555555")
print(user1)    # Alice
user2 = users.get("+33333333", "Unknown user")
print(user2)    # Bob
user3 = users.get("+44444444", "Unknown user")
print(user3)    # Unknown user

####### Удаление элемента

users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
 
del users["+55555555"]
print(users)    # { "+11111111": "Tom", "+33333333": "Bob"}

# Но стоит учитывать, что если подобного ключа не окажется в словаре, 
# то будет выброшено исключение KeyError.
# Поэтому опять же перед удалением желательно проверять наличие 
# элемента с данным ключом.
users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
 
key = "+55555555"
if key in users:
    del users[key]
    print(f"Элемент с ключом {key} удален")
else:
    print("Элемент не найден")

# pop(key): удаляет элемент по ключу key и возвращает удаленный элемент. Если элемент с данным ключом отсутствует, то генерируется исключение KeyError

# pop(key, default): удаляет элемент по ключу key и возвращает удаленный элемент. Если элемент с данным ключом отсутствует, то возвращается значение default

users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
key = "+55555555"
user = users.pop(key)
print(user)     # Alice
 
user = users.pop("+4444444", "Unknown user")
print(user)     # Unknown user

users.clear()

# Копирование и объединение словарей

# Метод copy() копирует содержимое словаря, возвращая новый словарь:
users = {"+1111111": "Tom", "+3333333": "Bob", "+5555555": "Alice"}
students = users.copy()
print(students)     # {"+1111111": "Tom", "+3333333": "Bob", "+5555555": "Alice"}

# Метод update() объединяет два словаря:

users = {"+1111111": "Tom", "+3333333": "Bob"}
 
users2 = {"+2222222": "Sam", "+6666666": "Kate"}
users.update(users2)
 
print(users)    # {"+1111111": "Tom", "+3333333": "Bob", "+2222222": "Sam", "+6666666": "Kate"}
print(users2)   # {"+2222222": "Sam", "+6666666": "Kate"}

####### Перебор словаря

users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
for key in users:
    print(f"Phone: {key}  User: {users[key]} ")

###### Метод items():
users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
for key, value in users.items():
    print(f"Phone: {key}  User: {value} ") # Возвращает ключ и значение

for key in users.keys():
    print(key)              #Вызывает ключи
    
for value in users.values():
    print(value)            # Перебирает значения
    
###### Комплексные словари

users = {
    "Tom": {
        "phone": "+971478745",
        "email": "tom12@gmail.com"
    },
    "Bob": {
        "phone": "+876390444",
        "email": "bob@gmail.com",
        "skype": "bob123"
    }
}
old_email = users["Tom"]["email"]
users["Tom"]["email"] = "supertom@gmail.com"
print(users["Tom"])     # { phone": "+971478745", "email": "supertom@gmail.com }

tom_skype = users["Tom"]["skype"]   # KeyErrorе, если нет - ошибка

# Чтобы избежать ошибки, можно проверять наличие ключа в словаре:

key = "skype"
if key in users["Tom"]:
    print(users["Tom"]["skype"])
else:
    print("skype is not found")    