# -*- coding: utf-8 -*-
# find a phone number without using regular expression

def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    
    if text[7] != '-':
        return False

    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print (is_phone_number('123-442-4342'))
print (is_phone_number('I don\'t want to learn python'))
