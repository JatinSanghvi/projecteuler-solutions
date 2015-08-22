"""
10001st prime

Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from math import exp


# Returns approximate sieve size based on prime number theorem.
def calculate_sieve_size(prime_index):
    for n in range(1, 1000):
        if prime_index < exp(n) / n:
            return int(1.25 * exp(n))


def prime_at_index(index):

    is_prime = [True] * calculate_sieve_size(index)
    sieve_size = len(is_prime)
    curr_index = 1

    for num in range(3, sieve_size, 2):

        if is_prime[num]:
            curr_index += 1
            if curr_index == index:
                return num

            for multiple in range(num * num, sieve_size, 2 * num):
                is_prime[multiple] = False


print prime_at_index(6)  # test
print prime_at_index(10001)  # solution
