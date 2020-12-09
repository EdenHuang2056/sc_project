"""
File: caesar.py
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Decipher the code using Caesar Cipher.
    """

    b = int(input('Secret number: '))
    # this number is how many numbers we shift

    old = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    new = ''
    # empty string to reset the new string

    new += old[26-b:]
    new += old[:26-b]

    c = input("What't the ciphered string? ")
    c = c.upper()
    d = ''
    for i in range(len(c)):
        k = new.find(c[i])
        if k == -1:
            d += c[i]
        else:
            d += old[k]

    print('The deciphered string is : ' + d)


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()

