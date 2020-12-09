"""
File: hangman.py
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    This code can let players guess the characters emerge randomly.
    Players can miss seven times until players guess the right character and win the game, otherwise
    players will be lose!

    """

    word = random_word()
    ans = ''
    for ch in word:
        if ch.isalpha():
            ans += '_'
    print('The world looks like: ' + str(ans))
    print('You have 7 guesses left')

    ans1 = ''
    life = N_TURNS
    while True:
        ch = input('Your guess: ')
        ch = ch.upper()
        i = word.find(ch)
        k = len(ch)
        if ch.isdigit():
            print('illegal format')
        elif ch.isalpha():
            if k != 1:
                print('illegal format')
            else:
                if i != -1:
                    for j in range(len(word)):
                        if ch == word[j]:
                            ans1 += ch
                        else:
                            ans1 += ans[j]
                    ans = ans1
                    ans1 = ''
                    print('You are correct!')
                    if ans == word:
                        print('')
                        print('You win!!')
                        print('')
                        print('-----')
                        print('| Thank you!!')
                        print('|   O')
                        print('| \\ | /')
                        print('|  / \\')
                        break
                    print('The world looks like: ' + str(ans))
                    print('You have ' + str(life) + ' guesses left')
                elif i == -1:
                    life -= 1
                    if life == 6:
                        print('-----')
                        print('|   |')
                        print('|')
                        print('|')
                        print('|')
                    elif life == 5:
                        print('-----')
                        print('|   |')
                        print('|   O')
                        print('|')
                        print('|')
                    elif life == 4:
                        print('-----')
                        print('|   |')
                        print('|   O')
                        print('|   |')
                        print('|')
                    elif life == 3:
                        print('-----')
                        print('|   |')
                        print('|   O')
                        print('| / |')
                        print('|')
                    elif life == 2:
                        print('-----')
                        print('|   |')
                        print('|   O')
                        print('| / | \\')
                        print('|')
                    elif life == 1:
                        print('-----')
                        print('|   |')
                        print('|   O')
                        print('| / | \\')
                        print('|  /')
                    else:
                        print('-----')
                        print('|   |')
                        print('|   O')
                        print('| / | \\')
                        print('|  / \\')
                    print('There is no ' + str(ch) + "'s in the word.")
                    if life != 0:
                        print('The world looks like: ' + str(ans))
                        print('You have ' + str(life) + ' guesses left')
                    else:
                        print('Your are completely hung :(', '\nThe word was: ' + word)
                        break


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()