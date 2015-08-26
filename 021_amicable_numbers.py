# coding: utf-8

"""
Amicable numbers

Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable
numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The
proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from operator import mul


def generate_factors(num):
    initial_num = num
    i = 2
    while i * i <= initial_num:
        power = 0
        while num % i == 0:
            num /= i
            power += 1

        if power > 0:
            yield i, power

        i += 1

    # Following condition will happen when largest prime factor is greater than square-root of number.
    if num > 1:
        yield num, 1


def generate_divisors(num):
    factors = list(generate_factors(num))
    num_factors = len(factors)
    powers = [0] * num_factors

    while True:
        yield reduce(mul, [factors[x][0] ** powers[x] for x in range(num_factors)], 1)

        i = 0
        while i < num_factors and powers[i] == factors[i][1]:
            powers[i] = 0
            i += 1

        if i == num_factors:
            return
        else:
            powers[i] += 1


def sum_divisors(num):
    # Do not consider the divisor equal to input number.
    return sum(list(generate_divisors(num))) - num


def all_amicable_numbers(limit):
    for num in range(2, limit):
        num2 = sum_divisors(num)
        if num2 != num and num == sum_divisors(num2):
            yield num


print sum(all_amicable_numbers(10000))
