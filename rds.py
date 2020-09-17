# GEO1000 - Assignment 2
# Authors: Pratyush Kumar
# Studentnumbers: 5359252

#%%
import string

#%%
def sentence_value(sentence):
    refined = ''.join([_ for _ in sentence.lower() if _.isalpha()])
    charlist = list('abcdefghijklmnopqrstuvwxyz')
    numlist = [_ for _ in range(1,27)]
    dic = {}
    for i in zip(charlist, numlist):
        dic[ i[0] ] = i[1]
    s=0
    for _ in refined:
        s+= dic[_]
    return int(s)


def rds(value):
    value=int(value)
    if(int(value/10) == 0): #already a single digit
        return(value)
    else:
        newnum = int(sum([int(i) for i in list(str(value)) ]))
        return(rds(newnum))


#%%
if __name__ == "__main__":
    initial_integer = sentence_value("Geomatics is fun!")
    result = rds(initial_integer)
    print(result)

# %%
