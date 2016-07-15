# -*- coding: utf-8 -*-
from random import randint
a = randint(1, 8)
Bingo = False

def number_comparing(a, b):
    if a == b:
        print ('you did it')
        return True
    elif a > b:
        print ('your number %d is too small'%(b))
        return False
    else:
        print ('your number %d is too big'%(b))
        return False

while Bingo == False:
    b = int(input('please enter your number >>>  '))
    Bingo = number_comparing(a, b)

# how to distinguish True or Flase
a = True
print (not a)       # it must be False
b = False
print (a and b)     # it is False
print (a or b)      # it is True