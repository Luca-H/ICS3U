"""
Name: Luca Hudici
Filename: Hour Converter
Purpose of program: To convert 24-hour format to 12-hour format
Date:
"""
import math
import time
import random

input("Press enter to continue...")
hour = 0
while(hour < 1 or hour > 24):
    hour = int(input("Please enter an hour between 1-24 only.\n"))

if(hour > 12):
    hour -= 12
    print("It is:",hour,"pm.")

else:
    print("It is:",hour,"am.")
