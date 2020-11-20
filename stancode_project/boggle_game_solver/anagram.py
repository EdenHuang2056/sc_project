"""
File: anagram.py
Name: Eden
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'     # This is the filename of an English dictionary
EXIT = '-1'                 # Controls when to stop the loop

count = 0
word_list = []              # The input words' index put in this list
chosen_list = []            # The letter program choose will be put in this list
python_list = []            # Take the words in dictionary to this list
answer_list = []            # The anagrams this program find


def main():
    global word_list, chosen_list, python_list, answer_list

    read_dictionary()
    print('Welcome to stanCode "Anagrams Generator" (or ' + str(EXIT) + ' to quit) ')

    while True:
        word = input('Find anagrams for: ')
        if word == EXIT:
            break

        print('Searching...')
        find_anagrams(word)

        print(f"{len(answer_list)} anagrams: {answer_list}")

        word_list = []
        answer_list = []


def read_dictionary():
    global python_list
    with open(FILE, 'r') as f:
        for line in f:
            line = line.split()
            python_list += line


def find_anagrams(s):
    """
    This function use recursion to find all the possible permutations of s (the user input).
    :param s: string, the user input word
    :return: nothing / this function only adds words into the global variable'searching_list'
    """

    # Take the index of input word to word_list
    for i in range(len(s)):
        word_list.append(i)

    find_anagrams_helper(s)


def find_anagrams_helper(s):
    global count, answer_list, word_list, chosen_list

    if len(chosen_list) == len(word_list):

        # Use index to convert into words
        ans = ''
        for ch in chosen_list:
            ans += s[ch]

        if ans in python_list and ans not in answer_list:
            answer_list.append(ans)
            print(ans)
            print('Searching...')

    else:
        answer = ''
        if has_prefix(answer) is True:
            for j in range(len(word_list)):
                element = word_list[j]

                if element not in chosen_list:

                    chosen_list.append(element)
                    answer += s[element]
                    find_anagrams_helper(s)

                    chosen_list.pop()


def has_prefix(sub_s):

    global word_list, chosen_list, python_list

    """
    This function can make sure that the current string(recorded in index) is in the dictionary.
    (or it will return False and stop finding.
    :param sub_s: a sub_string we want to search
    :return: (bool) If there is any words with prefix stored in current list(recorded in index)
    """

    for word in python_list:
        if word.startswith(sub_s) is True:
            return True
    return False


if __name__ == '__main__':
    main()
