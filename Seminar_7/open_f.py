with open(r'Seminar_7\\driver.txt','w', encoding='UTF-8') as f:
    f.write('driwer1,Ivanov\n')
    f.write('driwer2,Petrov')
    
with open(r'Seminar_7\\bus.txt','w', encoding='UTF-8') as d:
    d.write('bus1,E489MT\n')
    d.write('bus2,K715MO')
    
with open(r'Seminar_7\\marsrut.txt','w', encoding='UTF-8') as k:
    k.write('m1,1,bus1,driver1\n')
    k.write('m2,10,bus2,driver2\n')
    k.write('m3,7,bus2,driver1\n')
    
    
open(r'Seminar_7\\menu.py','w', encoding='UTF-8')