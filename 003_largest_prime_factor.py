"""
Largest prime factor

Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def largest_prime_factor(num):
    factor = 2
    while factor <= num / factor:
        if num % factor == 0:
            num /= factor
        else:
            factor += 1

    return num

print largest_prime_factor(13195)  # test
print largest_prime_factor(600851475143)  # solution
