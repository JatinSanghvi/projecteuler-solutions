"""
Counting Sundays

Problem 19

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""


def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


regular_year_days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year_days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Day of 1 Jan 1901. 1 is for Monday.
day = (1 + sum(leap_year_days_per_month if is_leap_year(1900) else regular_year_days_per_month)) % 7
sundays = 0

for year in range(1901, 2001):
    days_per_month = leap_year_days_per_month if is_leap_year(year) else regular_year_days_per_month
    for days in days_per_month:
        if day == 0:
            sundays += 1
        day = (day + days) % 7

print sundays
