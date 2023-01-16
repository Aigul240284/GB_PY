# with open('file.txt', 'a') as data: #разрывается без close
#  data.write('line 3 read\n')
#  data.write('line 4 read\n')
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# data.writelines(colors) # разделителей не будет
# data.write('\n LINE\n')
# data.write('LINE3\n')
# data.close()



# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#  print(line)
# data.close()
# exit()
import hello as h
print(h.f(1))

def new_string(symbol, count=3):
    return symbol*count
print(new_string(("!"), 5))
print(new_string('!'))
print(new_string(4))

def concatenatio(*params):
    res: str = ''
    for item in params:
        res+=item
    return res
print(concatenatio('a','s','d','w'))
print(concatenatio('a','1'))
print(concatenatio(1,2,3,4))
