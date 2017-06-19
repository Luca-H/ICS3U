"""
Name: Luca Hudici
Filename: Postage Calculator
Purpose of program: To calculate cost of postage based on weight
Date: 3/22/17
"""
import math
import time
import random

input("Welcome to postage calculator! Press next to continue...")
weight = 0
while(weight < 1):
    print("The prices are as following: \nUp to 30g ($0.48) \nUp to 50g ($0.70) \nUp to 100g ($0.90) \nPast 100g (100g cost + $0.18 per 50g)")
    weight = int(input("Please enter the weight of you package in grams:\n"))
    if(weight < 1):
        print("That is not a valid weight.")
#while loop used to detect invalid weights
if(weight <= 30):
    price = 0.48

elif(50 >= weight > 30):
    price = 0.70

elif(100 >= weight > 50):
    price = 0.90

elif(weight > 100):
    price = (((weight - 101) // 50 + 1) * 0.18) + 0.90

else:
    print("Oops! You may not have entered only numbers.")
#else statement used to detect any other invalid inputs

print("Your price comes to: $",price)
