"""
Name: Luca Hudici
Filename: Leap Year Calculator
Purpose of program: To determine if a year is leap year.
Date: 3/21/17
"""
import math
import time
import random

input("Welcome to Leap Year Calculator release 1.0! Press next to continue...")
year = int(input("Please enter a year anywhere from -7500 to 2100.\n"))

if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print(year, "is a leap year.(It has 366 days. )")

        else:
            print(year,"is not a leap year.(It has 365 days.)")

    else:
        print(year, "is a leap year.(It has 366 days. )")

else:
    print(year,"is not a leap year.(It has 365 days.)")
