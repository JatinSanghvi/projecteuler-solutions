# coding=utf-8

"""
Largest palindrome product

Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from datetime import datetime


def is_palindrome(num):
    return str(num) == str(num)[::-1]


def largest_palindrome():

    largest_product = 100000
    for i in range(999, 99, -1):
        for j in range(999, i - 1, -1):
            product = i * j
            if product <= largest_product:
                if j == 999:
                    return largest_product
                else:
                    break

            if is_palindrome(product):
                largest_product = max(product, largest_product)

start_time = datetime.now()
print largest_palindrome()
print datetime.now() - start_time
