l_t1=[i for i in range(1,11)]
l_t2=[]
for i  in range(1,11):
    l_t2.append(i)

print(l_t1)
print(l_t2)
l_t3=[i for i in range(1,11) if i%2==0]
print(l_t3)
l_t3=[(i,i) for i in range(1,11) if i%2==0]
print(l_t3)
l_t3=[i*2 for i in range(10) if i%2==0]
print(l_t3)