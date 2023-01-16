# # List comprehension
# [exp for item in iterablle]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

list =[]
for i in range (1,10):
    if(i%2 ==0):
        list.append(i)
print(list)

list = [i for i in range(1,10) if i%2==0]
print(list)
list = [(i,i) for i in range(1,10) if i%2==0]
print(list)

def f(x):
    return x**3

list = [(i,f(i)) for i in range(1,21)if i%2==0]
print(list)