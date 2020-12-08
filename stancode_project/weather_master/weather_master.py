"""
File: weather_master.py
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100
# this is the constant let we can exit the code


def main():
	"""
	This is a Temperature information processor,
	which allows users input their temperature information.
	At the end, it will show the highest and the lowest temperature.
	It also calculates the average temperature
	and the number of cold days, which represent the days under 16 degrees.
	"""

	average = 0
	# This number can record how many data we input.

	total = 0
	# This number can calculate the total temperature we input.

	cold = 0
	# this number can record the cold day(s)

	print('stanCode \"Weather Master 4.0!\"')

	temperature = int(input('Next Tempterature: (or ' + str(EXIT) + ' to quit)? ' ))

	if temperature == EXIT:
		# we input EXIT constant first and we can exit
		print('No temperature were entered.')

	else:
		maximum = temperature
		minimum = temperature
		total = temperature
		# I put the first temperature to maximum, minimum and total

		average += 1

		while True:
			temperature = int(input('Next Tempterature: (or ' + str(EXIT) + ' to quit)? '))

			if temperature < 16:
				cold += 1
				# if temperature is lower than 16, the cold number will add one

			if temperature == EXIT:
				break
			else:
				average += 1
				total = total + temperature
				if temperature > maximum:
					maximum = temperature

				elif temperature < minimum:
					minimum = temperature

				else:
					pass

		average = total / average
		print('Hightest temperature is = ' + str(maximum))
		print('Lowest temperature is = ' + str(minimum))
		print('Average = ' + str(average))
		print(str(cold) + ' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()

