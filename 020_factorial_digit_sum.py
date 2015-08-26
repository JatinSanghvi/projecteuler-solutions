# coding: utf-8

"""
Factorial digit sum

Problem 20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

from math import factorial


def factorial_digit_sum(num):
    return sum([int(digit) for digit in str(factorial(num))])


print factorial_digit_sum(10)  # test
print factorial_digit_sum(100)  # solution
