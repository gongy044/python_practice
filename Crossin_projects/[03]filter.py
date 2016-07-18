# -*- coding: utf-8 -*-

def load_bloaked():
    global bloaked_words
    bloaked_words = []
    with open('bloaked.txt') as f:
        lines = f.readlines()
        for line in lines:
            bloaked_words.append(line.strip())

def text_filter(text, rep_symbol = '*'):
    for word in bloaked_words:
        a =text.replace(word, rep_symbol*len(word.encode()))
    return a

if __name__ == '__main__':
    print ('you can filter text before you publish it')
    text = input('what do you want to filter:  ')
    print ('=====wait a sec.=====')
    load_bloaked()
    print (text_filter(text))
else:
    print ('fuck off')