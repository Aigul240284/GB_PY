# colors=["red","green","blue"]
# data=open(r'instruction_py\L_fils\\file.txt','a',encoding='UTF-8')
# data.writelines(colors)
# data.close()

# with open(r'instruction_py\L_fils\\file.txt','w') as data:
#     data.write('line 1\n')
#     data.write('line 1\n')
    
path=r'instruction_py\L_fils\\file.txt' 
data=open(path,'r')
for line in data:
    print(line)
data.close()
    