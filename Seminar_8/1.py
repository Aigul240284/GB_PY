s='10 * 2 - 4 + 10 * 10'.split()
# s=n.split()
# m2=[]
# print(m)

def calc(lt):
    for i in range(len(lt)+1):
        if i == '*': 
            result=lt[i-1]*lt[i+1]
            lt[i]=result
        elif i == '/': 
            result=lt[i-1]/lt[i+1]
            lt[i]=result
        print(lt)
        
        
            
            
#         return a+b
#     elif ch == '-':
#         return a-b
#     elif ch == '*':
#         return a*b
#     elif ch == '/':
#         return a/b
    
# result= int(s[0])

# for i in range(1, len(m)-1,2):
#     if m[i]=='*' or m[i]=='/':
#         result=calc(int(m[i-1]), int(m[i+1]),m[i])
#         m2.append(result)
#     else:
#         m2.append(m[i])
#         m2.append(m[i+1])
#     # print(m[i],m[i+1])
# print(m2)
#     # print(result)
# for i in range(1, len(m2)-1,2):
#     if i!='-' or i!= '+' or i !='*' or i!='/':
#         m2.pop(i)
#     print(m2)
# s = '10/2+5*2'
num = ''
old_list = []


for i, elem in enumerate(s):
    if elem.isdigit():
        num += elem
    # elif elem in '()':
    #     old_list.append(elem)
    else:
        old_list.append(int(num))
        old_list.append(elem)
        num = ''
# if s[-1] == ')':
#     old_list.insert(-1, int(num))
else:
    old_list.append(int(num))

# if '(' in old_list:
#     first_i = old_list.index('(')
#     second_i = old_list.index(')')
#     old_list = old_list[:first_i] + \
#         calc(old_list[first_i+1:second_i])+old_list[second_i+1:]

print(calc(old_list))
        
    
    