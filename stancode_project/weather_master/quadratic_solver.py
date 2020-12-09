"""
File: quadratic_solver.py
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	The codes following are asking users to input a, b, c respectively
	to compute the roots of equation ax^2 + bx + c = 0.
	At the end, it would come up with three types of answer,
	one root, two roots and no real roots.
	"""

	# input the coefficient of the formula.
	print('stanCode Quadratic solver! ')
	a = int(input('Enter a : '))
	b = int(input('Enter b : '))
	c = int(input('Enter c : '))

	d = (b ** 2)-(4 * a * c)

	if d > 0:
		# calculate the two real roots
		print('Two roots: ', end="")
		g = math.sqrt(d)
		e = (-b + g) / (2*a)
		f = (-b - g) / (2*a)

		print(str(e)+' , '+str(f))

	elif d == 0:
		# calculate the one real root
		print('One root: ', end="")
		e = (-b) / (2*a)

		print(str(e))

	else:
		print('No real roots')


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == "__main__":
	main()
