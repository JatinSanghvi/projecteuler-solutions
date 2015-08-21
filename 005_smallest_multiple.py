"""
Smallest multiple

Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def greatest_common_divisor(num1, num2):
    if num1 % num2 == 0:
        return num2
    else:
        return greatest_common_divisor(num2, num1 % num2)


def least_common_multiple(num1, num2):
    return num1 * num2 / greatest_common_divisor(num1, num2)


def smallest_multiple(limit):

    result = 1
    for num in range(2, limit + 1):
        result = least_common_multiple(result, num)

    return result

print smallest_multiple(10)  # test
print smallest_multiple(20)  # solution
