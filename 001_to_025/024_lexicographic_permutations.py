"""
Lexicographic permutations

Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3
and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from math import factorial


def permutation(digits, sequence_num):

    if sequence_num == 0:
        return digits
    else:
        divisor = factorial(len(digits) - 1)
        pos = sequence_num / divisor
        return digits[pos] + permutation(digits[:pos] + digits[pos + 1:], sequence_num % divisor)


def print_permutation(digits, sequence_num):
    print permutation(digits, sequence_num - 1)


# test
for sequence_num in range(1, 7):
    print_permutation("012", sequence_num)

# solution
print_permutation("0123456789", 1000000)
