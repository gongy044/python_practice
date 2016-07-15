# -*- coding: utf-8 -*-
# set two variables, and compare them
a = int(input('please enter number a >>>  '))
b = int(input('please enter number b >>>  '))

def number_comparing(a, b):
    if a == b:
        print ('pretty good')
    elif a > b:
        print ('number a is greater than b')
    else:
        print ('number a is smaller than b')

number_comparing(a, b)
