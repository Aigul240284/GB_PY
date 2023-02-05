with open(r'mihail\\new_file.txt','w', encoding='UTF-8') as f:
    f.write('1 2 3 4 5 \n 6 8 9 10\n')
    f.write('77 78 79')
    
    
path = r'mihail\\new_file.txt'
data = open(path,'r')
num_row=[]
for line in data:
    num_row+=list(map(int,line.split()))
    print(line)
data.close()
print(num_row)

for i, elem in enumerate(num_row[:-1]):
    if elem+1!=num_row[i+1]:
        print(elem+1)
        
for i in range(0,num_row[:-1]):
    if num_row[i]+1!=num_row[i+1]:
        print(num_row[i]+1)

        
        
        
    