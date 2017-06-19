"""
Name: Luca Hudici
Filename: Credit Card Eligibility Calculator
Purpose of program: To determine someone's eligibility for a credit card.
Date: 3/23/17
"""
import math
import time
import random

input("Welcome to Credit Card Eligibility Calculator! Press enter to continue...")
redo = 1
points = 0
#redo variable with while used to detect errors and give user a chance to try again
while(redo == 1):
  age = int(input("Please enter your age: \n"))
  address = float(input("How many years have you spent at your current address: \n"))
  income = int(input("How much money do you make per year on average: \n"))
  job = float(input("How many years have you spent at your current job: \n"))

  if(0 < age < 20):
      points -= 10
      redo = 0
  elif(20 < age <= 30):
      points += 0
      redo = 0
  elif(31 <= age <= 50):
      points += 20
      redo = 0
  elif(age > 50):
      points += 25
      redo = 0
  else:
      redo = 1
      print("You might have made a typo or otherwise entered invalid info. Please try again.")
      time.sleep(1)

  if(address < 1):
      points -= 5
      redo = 0
  elif(1 <= address <= 3):
      points += 5
      redo = 0
  elif(4 <= address <= 8):
      points += 12
      redo = 0
  elif(address > 8):
      points += 20
      redo = 0
  else:
      redo = 1
      print("You might have made a typo or otherwise entered invalid info. Please try again.")
      time.sleep(1)

  if(income < 15000):
      points += 0
      redo = 0
  elif(15000 <= income < 25000):
      points += 12
      redo = 0
  elif(25000 <= income < 40000):
      points += 24
      redo = 0
  elif(income >= 40000):
      points += 30
      redo = 0
  else:
      redo = 1
      print("You might have made a typo or otherwise entered invalid info. Please try again.")
      time.sleep(1)

  if(job < 2):
      points -= 4
      redo = 0
  elif(2 <= job < 4):
      points += 8
      redo = 0
  elif(job >= 4):
      points += 15
      redo = 0
  else:
      redo = 1
      print("You might have made a typo or otherwise entered invalid info. Please try again.")
      time.sleep(1)

  if(points < 20):
      print("You do not meet the minimun criteria to have enough points to get a card.\nYou have:",points,"points.")
  elif(20 <= points <= 35):
      print("You get a credit card with a $500 limit.\nYou have:",points,"points.")
  elif(36 <= points <= 60):
      print("You get a credit card with a $2000 limit.\nYou have:",points,"points.")
  elif(points > 60):
      print("You get a credit card with a $5000 limit.\nYou have:",points,"points.")

print("Thanks for using Credit Card Eligibility Calculator!")
