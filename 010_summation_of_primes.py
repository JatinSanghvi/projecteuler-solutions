"""
Summation of primes

Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def sum_of_primes(limit):
    is_prime = [True] * limit
    total = 2

    for num in range(3, limit, 2):
        if is_prime[num]:
            total += num
            for multiple in range(num * num, limit, 2 * num):
                is_prime[multiple] = False

    return total

print sum_of_primes(10)  # test
print sum_of_primes(2000000)  # solution
