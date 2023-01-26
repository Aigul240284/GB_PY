# Есть код который не можем менять
# transformation=<???>
# values = [2,3,5,7,11,13,17,19,23,29]
# transformed_values=list(map(transformation,values))
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values

values = [2,3,5,7,11,13,17,19,23,29]
transformation= lambda x:x

transformed_values=list(map(transformation,values))
values[1]=1 #для проверки что копия
print(values)
print(transformed_values)