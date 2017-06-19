"""
Name: Luca Hudici
Filename:  Zodiac Calculator 64
Purpose of program: To calculate your zodiac symbol
Date: 3/21/17
"""
import math
import time
import random

input("Welcome to Zodiac calculator 64! Press next to continue...")

day = 0

redo = 1

while(31 < day < 1 or redo == 1):

    month = input("Please enter what month you were born in lower case and without spaces before or after: \n")

    day = int(input("Please enter what day of the month you were born: \n"))
#while loop used to detect invalid dates

    if((month == "march" and 31 >= day >= 21) or (month == "april" and 19 >= day >= 1)):
        print("You are an Aries: The Ram. I bet your computer likes you a lot.")
        redo = 0
    elif((month == "april" and 30 >= day >= 20) or (month == "may" and 20 >= day >= 1)):
        print("You are a Taurus: The Bull.")
        redo = 0
    elif((month == "may" and 31 >= day >= 21) or (month == "june" and 21 >= day >= 1)):
        print("You are Gemini: The Twins.")
        redo = 0
    elif((month == "june" and 30 >= day >= 22) or (month == "july" and 22 >= day >= 1)):
        print("You are Cancer: The Crab.")
        redo = 0
    elif((month == "july" and 31 >= day >= 23) or (month == "august" and 22 >= day >= 1)):
        print("You are Leo: The Lion. Rawr.")
        redo = 0
    elif((month == "august" and 31>= day >= 23) or (month == "september" and 22>= day >=1)):
        print("You are Virgo: The Virgin.")
        redo = 0
    elif((month == "september" and 30 >= day >= 23) or (month == "october" and 23 >= day >= 1)):
        print("You are Libra: The Scales. You should be a judge.")
        redo = 0
    elif((month == "october" and 31 >= day >= 24) or (month == "november" and 21 >= day >= 1)):
        print("You are Scorpio: The Scorpion.")
        redo = 0
    elif((month == "november" and 30 >= day >= 22) or (month == "december" and 21 >= day >= 1)):
        print("You are Sagittarius: The Archer. You might do well in CS:GO")
        redo = 0
    elif((month == "december" and 31 >= day >= 22) or (month == "january" and 19 >= day >= 1)):
        print("You are are Capricorn: The Goat. Ba-a-a-a-ah.")
        redo = 0
    elif((month == "january" and 31 >= day >=20) or (month == "febuary" and 18 >= day >= 1)):
        print("You are Aquarius: The Water Bearer. Glug, glug, glug, don't get on a boat.")
        redo = 0
    elif((month == "febuary" and 19 >= day >= 1) or (month == "march" and 20 >= day >= 1)):
        print("You are Pisces: The Fish.")
        redo = 0
    else:
        print("You must have entered an invalid date either by typo or not using lowercase. \nPlease try again:")
        redo = 1
#Redo variable used to detect other invalid dates
print("Thank you for using Zodiac Calculator 64!")
