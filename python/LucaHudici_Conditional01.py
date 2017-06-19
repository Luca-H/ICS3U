"""
Name: Luca Hudici
Filename:Numbers for Dummies
Purpose of program: To determine the class of a number
Date: 3/21/17
"""
import math;
import time;
import random;

input("Welcome to Numbers for Dummies release 1.0! Press enter to continue...");

number = int(input("Enter a number, any number...\n"));

if(number < 0):
    negativity = "Negative";

elif(number == 0):
    negativity = "0"

else:
    negativity = "Positive";

equality = number % 2;

if(equality != 0):
    decimal = "Odd"

else:
    decimal = "Even"

print("Your number is:", negativity, "and", decimal);
