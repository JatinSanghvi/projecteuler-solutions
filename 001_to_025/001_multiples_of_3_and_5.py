"""
Multiples of 3 and 5

Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_of_multiples(num, limit):
    num_of_multiples = (limit - 1) / num
    return num * (num_of_multiples * (num_of_multiples + 1) / 2)


print sum_of_multiples(3, 10) + sum_of_multiples(5, 10) - sum_of_multiples(15, 10)  # test
print sum_of_multiples(3, 1000) + sum_of_multiples(5, 1000) - sum_of_multiples(15, 1000)  # solution
