"""
Non-abundant sums

Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the
sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two
abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as
the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is
known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
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


def get_abundant_numbers():
    for num in range(12, 28124):
        if sum_divisors(num) > num:
            yield num


def list_sum_of_two_abundant_numbers():
    abundant_numbers = set()
    sum_of_two_abundant_numbers = set()

    for num in get_abundant_numbers():
        abundant_numbers.add(num)
        [sum_of_two_abundant_numbers.add(num + num2 if num + num2 < 28124 else 0) for num2 in abundant_numbers]

    return sum_of_two_abundant_numbers


def get_non_sum_of_two_abundant_numbers():
    last_num = 1
    for num in list_sum_of_two_abundant_numbers():
        while last_num < num:
            yield last_num
            last_num += 1
        last_num = num + 1

print sum(get_non_sum_of_two_abundant_numbers())
