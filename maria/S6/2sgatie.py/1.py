from itertools import groupby, starmap
from os import path

def rle_encode (text='text_words.txt', code_text="text_code_words.txt"):
    if path.exists(text):
        with open(r'maria\\text_words.txt') as my_f_1, \
                open(r'maria\\text_code_words.txt', 'a') as my_f_2:
            for i in my_f_1:
                my_f_2.write(''.join([f'{len(list(v))}{ch}' for ch, v in groupby(i)]))
    else:
        print("The files do not exist in the system")
        
print(rle_encode())

        