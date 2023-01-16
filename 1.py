import random
array = list(random.randint(1, 10) for i in range(4))
print(array)
max_n = 0
# print(len(array))
for i in range(0,len(array)-2):
    # print(array[i])
    nam = array[i]+array[i+1]+array[i+2]
    if nam > max_n:
        max_n = nam
print(max_n)

# max_B = 0
# # list_2 = []
# list_1 = list(random.randint(1, 5) for i in range(4))

# for i in range(len(list_1)-1):
#     harvest = list_1[i-1]+list_1[i]+list_1[i+1]
#     if harvest > max_B:
#         max_B = harvest
#     print(harvest, end="  ")
# last_harvest = list_1[0]+list_1[-1]+list_1[-2]
# if last_harvest > max_B:
#     max_B = last_harvest
# print(last_harvest)
# print(max_B)

