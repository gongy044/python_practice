# -*- coding: utf-8 -*-
import os

def find_file(key_word, inputpath = '.'):
	finded_file = []
	for (path, dirnames, filenames) in os.walk(inputpath):
		for name in filenames:
			full_name = os.path.join(path, name)
			if key_word in name:
				finded_file.append(full_name)
			with open(full_name) as f:
				for line in f.readlines():
					if key_word in line:
						finded_file.append(full_name + ':' + line)
	return finded_file

inputpath = input('path is :  ')
key = input('what do you want to search for? >>>  ')
result = find_file(key, inputpath)

for i in result:
	print (i)
			