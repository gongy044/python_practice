# -*- coding: utf-8 -*-
from random import randint

with open('data.txt', 'r') as f:
	lines = f.readlines()

# print (lines)
scores = {}
for line in lines:
	line_list = line.split()
	scores[line_list[0]] = line_list[1:]
# print (scores)

user_name = input('what\'s your name? >>>  ')
score = scores.get(user_name)
if score is None:
	scores[user_name] = ['0', '0']
	
times = int(scores[user_name][0])
times += 1
scores[user_name][0] = str(times)
score = int(scores[user_name][1])
print ('you have played %d times, and your score is %d'%(times, score))

def number_comparing(a, b):
	if a == b:
		global score, a
		score += 1
		scores[user_name][1] = str(score)
		print ('you did it, now your score is %d'%(score))
		_continue = input('one more round? y/n >>>  ')
		if _continue == 'y':
			return False
		else:
			result = ''
			for name in scores:
				line = name + ' ' + ' '.join(scores[name]) + '\n'
				result += line
			with open('data.txt', 'w') as f:
				f.write(result)
			return True
	elif a > b:
		print ('your number is too small')
		return False
	else:
		print ('your number is too big')
		return False

a = randint(1, 8)
Bingo = False

while Bingo == False:
	b = int(input('please enter a number between 1-8, negative number for quitting'))
	if b < 0:
		result = ''
		for name in scores:
			line = name + ' ' + ' '.join(scores[name]) + '\n'
			result += line
		with open('data.txt', 'w') as f:
			f.write(result)
		print ('game over')
		break
	Bingo = number_comparing(a, b)
					

