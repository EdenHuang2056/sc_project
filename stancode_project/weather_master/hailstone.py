"""
File: hailstone.py
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, as defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program present the process of Hailstone sequence.
    Users allowed to input a integer n, n > 0.
    At the end, it will always stop with 1, and showing how many steps it went through.

    """
    a = int(input('Enter a number :'))
    b = 0   # I can use this number to calculate how many steps we do.

    while a > 1:
        if a % 2 == 1:
            # the input number is odd, if it enter this loop,  step will add one
            print(str(a) + ' is odd , ', end="")
            a = 3*a+1
            print('so I make 3n+1: ' + str(a))
            b += 1

        else:
            # the input number is even, if it enter this loop,  step will add one
            print(str(a) + ' is even , ', end="")
            a = a / 2
            print('so I take half: ' + str(a))
            b += 1

    print('It took ' +str(b) + ' steps to reach 1.')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()