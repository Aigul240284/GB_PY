from random import sample

def list_rand_words (count:int, alp:str='абв'):
    words_list=[]
    for i in range(count):
        letters=sample(alp, k=3)
        words_list.append("",join(letters))
    return " ".join(words.list)
list_rand_words(4)