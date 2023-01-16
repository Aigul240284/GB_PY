def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
list =[] 
for e in range(1,10):
    list.append(fib(e))
print(list)
print(fib(4))

a,b=3,4
print('a=', a)
s=(3,4)
print(s[-1])