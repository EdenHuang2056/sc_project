"""
File: similarity.py
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    Print the most similarity sequence input with target sequence
    """

    long = input("Please give me a DNA sequence to search: ")

    long = long.upper()

    short = input("What DNA sequence would you like to match? ")

    short = short.upper()

    max_d = 0
    maximum_dna = ''

    for i in range(len(long)-len(short)+1):
        # how many times need to compare
        sub_long = long[i:i+len(short)]
        d = 0
        # record how many dna be corresponded
        for j in range(len(short)):
            # how many letter need to record
            if short[j] == sub_long[j]:
                d += 20
        if d > max_d:
            max_d = d
            maximum_dna = sub_long
    # print(str(max_d))

    print(maximum_dna)


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()