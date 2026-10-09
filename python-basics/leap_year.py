"""Leap year check.

A year is a leap year if it is divisible by 4 and not by 100,
or it is divisible by 400.
"""

n = int(input())

if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    print("leap")
else:
    print("not a leap")
