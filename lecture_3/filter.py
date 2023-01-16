data = [x for x in range(10)]
print(data)

res = list(filter(lambda x: not x%2, data))
print(res)

data = '1 2 3 5 8 15 23 38'.split()
print(data)
res = map(int, data) # map вместо select
# print(res)

res = filter(lambda e: not e % 2, res)
res = list(map(lambda e: (e, e**2), res))
print(res)