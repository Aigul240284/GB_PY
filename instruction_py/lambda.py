a=[1,2,3,5,8,15,23,38]
b=[(i,i*i) for i in a if i%2==0]
print(b)

def select(f,col):
    return[f(x) for x in col]

def where(f,col):
    return[x for x in col if f(x)]
data=[1,2,3,5,8,15,23,38]
# res=select(int, data)
# print(res)

# res=where(lambda x:x%2==0,data)
# print(res)
# res=select(lambda x:(x,x**2),res)
# print(res)
data=list(map(lambda x: (x,x**2), filter(lambda x:x%2==0, data)))






