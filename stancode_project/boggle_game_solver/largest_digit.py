"""
File: largest_digit.py
Name: Eden
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""
maximum = 0


def main():

	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	This function will call the helper function to achieve the final goal.
	:param n: int, the integer
	:return: int, the biggest digit in the integer
	"""
	global maximum

	maximum = 0

	# Confirm the number is plus
	if n < 0:
		n = -n
	find_largest_digit_helper(n)

	return maximum


def find_largest_digit_helper(n):

	global maximum

	if n < 10:
		if n > maximum:
			maximum = n
		return
	else:
		if n % 10 > maximum:
			maximum = n % 10
		find_largest_digit_helper(n//10)


if __name__ == '__main__':
	main()
