"""
File: complement.py
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """

    This code can let user to find the complement DNA.

    """
    dna = input("Please give me a DNA and strand and I'll find the complement: ")
    dna = dna.upper()
    new_dna = build_complement(dna)
    print('The complement of ' + dna + ' is ' + str(new_dna))


def build_complement(dna):
    ans = ''
    for base in dna:
        if base == 'A':
            ans += 'T'

        elif base == 'T':
            ans += 'A'

        elif base == 'C':
            ans += 'G'

        elif base == 'G':
            ans += 'C'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()