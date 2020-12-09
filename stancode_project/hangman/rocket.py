"""
File: rocket.py
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

SIZE = 10


def main():
	head()
	belt()
	body_up()
	body_down()
	belt()
	head()


def head():
	row = SIZE
	column = SIZE
	for i in range(row):
		print(' ', end='')
		for j in range(column-i-1):
			print(' ', end='')
		for k in range(1+i):
			print('/', end='')
		for l in range(i+1):
			print('\\', end='')
		for m in range(column-i-1):
			print(' ', end='')
		print(' ')


def belt():

	print('+', end='')
	for i in range(SIZE*2):
		print('=', end='')
	print('+')


def body_up():

	row = SIZE
	column = SIZE

	for i in range(row):
		print('|', end='')
		for j in range(column-i-1):
			print('.', end='')
		for k in range(i+1):
			if k % 2 == 1:
				print('\\', end='')
			else:
				print('/', end='')
		for l in range(i+1):
			if i % 2 == 0:
				if l % 2 == 1:
					print('/', end='')
				else:
					print('\\', end='')
			else:
				if l % 2 == 1:
					print('\\', end='')
				else:
					print('/', end='')

		for m in range(column-i-1):
			print('.', end='')
		print('|', end='')
		print('')


def body_down():

	row = SIZE
	column = SIZE

	for i in range(row):
		print('|', end='')
		for j in range(i):
			print('.', end='')
		for k in range(column-i):
			if k % 2 == 1:
				print('/', end='')
			else:
				print('\\', end='')
		for l in range(column-i):
			if SIZE % 2 == 0:
				if i % 2 == 0:
					if l % 2 == 1:
						print('/', end='')
					else:
						print('\\', end='')
				else:
					if l % 2 == 1:
						print('\\', end='')
					else:
						print('/', end='')
			else:
				if i % 2 == 0:
					if l % 2 == 1:
						print('\\', end='')
					else:
						print('/', end='')
				else:
					if l % 2 == 1:
						print('/', end='')
					else:
						print('\\', end='')

		for m in range(i):
			print('.', end='')
		print('|', end='')
		print('')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
