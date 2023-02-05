def fib(n):
    if n in [1,2]:
        return 1
    return fib(n-1)+fib(n-2)


L_t=[]
for i in range(1,10):
    L_t.append(fib(i))
print(L_t)