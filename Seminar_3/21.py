import os
os.system('cls')
# Задача №21

# Напишите программу для печати всех уникальных значений в словаре. 

# Input:  {"I": "S001", "II": "S002", "III": "S001", "IV": "S005", "V": "S005", "VI":"S009", "VII": "S007"}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
inpDict = {"I": "S001", "II": "S002", "III": "S001", "IV": "S005", 
           "V": "S005", "VI":"S009", "VII": "S007"}
rez=set(inpDict.values())
print(sorted(rez))

