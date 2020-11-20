"""
File: boggle.py
Name:Eden
----------------------------------------
This program can find all words in a 4x4 square grid which input by the user.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# global variable
python_list = []        # Take the words in dictionary to this list
big_list = []
tuple_list = []
count = 0				# Counting how many words we find.
answer_list = []		# This is the list of answer


def main():
	read_dictionary()
	input_word()
	for a in range(4):
		for b in range(4):
			tuple_list.append((a, b))
			answer = ''
			answer += big_list[a][b]
			anagrams(a, b, answer, tuple_list)
			tuple_list.clear()

	print(f"There are {count} words in total.")


def input_word():
	"""
	Input 16 letters we want to search for.
	"""
	for i in range(4):
		small_list = []
		input_words = input(str(i+1) + ' row of letters: ')
		if len(input_words) < 0 or len(input_words) > 7 or input_words[1] and input_words[3] and input_words[5] is not ' ':
			print('Illegal print')
			break
		for j in range(len(input_words)):
			if input_words[j].isdigit() is True:
				print('Illegal print')
				break
		else:
			for j in range(0, 8, 2):
				small_list.append(input_words[j].lower())
			big_list.append(small_list)


def read_dictionary():
	global python_list  # put the words of dictionary in python_list
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			line = line.split()
			python_list += line


def anagrams(x, y, answer, tuple_list):
	global big_list, count

	if len(answer) >= 4:
		if answer in python_list and answer not in answer_list:
			count += 1
			answer_list.append(answer)
			print('Found: "' + answer + '"')

	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			new_x = x+i
			new_y = y+j
			if 0 <= new_x <= 3 and 0 <= new_y <= 3:
				if (new_x, new_y) not in tuple_list:
					if has_prefix(answer) is True:

						tuple_list.append((new_x, new_y))
						answer += big_list[new_x][new_y]
						anagrams(new_x, new_y, answer, tuple_list)

						tuple_list.pop()
						answer = answer[:len(answer)-1]


def has_prefix(sub_s):
	"""

	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s

	"""
	for word in python_list:
		if word.startswith(sub_s) is True:
			return True
	return False


if __name__ == '__main__':
	main()
