"""
Number letter counts

Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one
hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
         "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def number_of_letter(num):
    num_letters = 0

    thousand = (num % 10000) / 1000
    if thousand > 0:
        num_letters += len(units[thousand]) + len("thousand")

    hundred = (num % 1000) / 100
    if hundred > 0:
        num_letters += len(units[hundred]) + len("hundred")

    and_ = (num / 100 > 0) and (num % 100 > 0)
    if and_:
        num_letters += len("and")

    ten = (num % 100) / 10
    if ten > 0 and ten != 1:
        num_letters += len(tens[ten])

    unit = num % 10
    if ten == 1:
        num_letters += len(units[ten * 10 + unit])
    elif unit > 0:
        num_letters += len(units[unit])

    return num_letters


def total_number_of_letters(from_, to):
    total_letters = 0
    for num in range(from_, to + 1, 1):
        total_letters += number_of_letter(num)

    return  total_letters


print total_number_of_letters(1, 5)  # test 1
print number_of_letter(342)  # test 2
print number_of_letter(115)  # test 3
print total_number_of_letters(1, 1000)  # test 1
