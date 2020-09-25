# GEO1000 - Assignment 2
# Authors: Pratyush Kumar & Michiel de Jong
# Studentnumbers: 5359252 & 4376978

import string

def sentence_value(sentence):
    """gives the sum of the positions of the letters in a sentence

    Args:
        sentence (string): string input by the user

    Returns:
        integer: summation of all positions of the letters in sentence var
    """ 
    refined = ''.join([_ for _ in sentence.lower() if _.isalpha()])
    charlist = string.ascii_lowercase #list('abcdefghijklmnopqrstuvwxyz')
    numlist = [_ for _ in range(1,27)]
    dic = {} # dictionary to map elements of  charlist to numlist
    for i in zip(charlist, numlist):
        dic[ i[0] ] = i[1]
    s=0
    for _ in refined:
        s+= dic[_]
    return int(s)


def rds(value):
    """returns summation of the number , repeats till single digit is obtained

    Args:
        value (int): number fed into rds from sentence_value frunction
    """
    value=int(value)
    if(int(value/10) == 0): #already a single digit
        return(value)
    else:
        newnum = int(sum([int(i) for i in list(str(value)) ]))
        return(rds(newnum))


if __name__ == "__main__":
    usr_inp =''
    usr_inp = input("Please enter a sentence and press return, \nTo go with the default sentence of \'Geomatics is fun!\' , just press return:  ")
    if usr_inp == '' :
        usr_inp = 'Geomatics is Fun!'
    initial_integer = sentence_value(usr_inp)
    result = rds(initial_integer)
    print(result)
