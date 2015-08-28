# coding=utf-8

"""
Sum square difference

Problem 6

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sum_square_difference(num):
    # summation over 1..n = n(n+1) / 2
    # summation over 1^2..n^2 = n(n+1)(2n+1) / 6
    # therefore, result = n^2 (n+1)^2 / 4 - n(n+1)(2n+1) / 6
    #                   = n(n+1) [3n(n+1) - 2(2n+1)] / 12
    #                   = n(n+1)(3n^2-n-2) / 12
    #                   = n(n+1)(n-1)(3n+2)/12

    return num * (num + 1) * (num - 1) * (3 * num + 2) / 12

print sum_square_difference(10)  # test
print sum_square_difference(100)  # solution
