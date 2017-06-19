"""
Name: Luca Hudici
Filename: ATM
Purpose of program: To withdrawl money, deposit money, view current balance, commit tax evasion, endless possibilities.
Date: Apr 26 2017
"""
import math
import time
import random
import csv

quit = "no"
balance = 1500

def welcome():
    print("Welcome to ATM.py build BETA 1.0!")
    input("Press enter to continue...")

def menu():
    choice = input("Type 'withdraw' to withdraw money\nType 'deposit' to make a deposit\nType 'balance' to view balance\nType 'exit' to exit the ATM\n")
    return(choice)

def exit():
    choice = input("Are you sure you want to quit?'yes' or 'no':\n")
    if choice == 'yes':
        exit = 'yes'
    else:
        exit = 'no'
    return(exit)

def withdraw(balance):
    case = "true"
    while case == "true":
        withdrawl = input("How much money would you like to withdraw?\n")
        valid = 0
        counter = 0
        #For loop created to verifiy that each character in the user's input is a number or decimal and not anything else
        for char in withdrawl:
            if(counter == 0 and char == '.'):
                print("Please put a number before a decimal.")
                valid = 0
                break
            if (char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9" or char == "0" or char == "."):
                valid = 1
            else:
                valid = 0
                break
            counter += 1
        if(valid == 0):
            print("Please use positive numbers only.")
            continue
        withdrawl = float(withdrawl)
        #second if statement created to not let user withdraw more than their balance.
        if(withdrawl > balance):
            print("You cannot put your balance in the negatives.")
            continue
        else:
            case = "false"
            withdrawl = float(withdrawl)
            balance -= withdrawl
            print("Please wait...")
            time.sleep(3)
            print("Done!\n")
            return(balance)


def deposit(balance):
    case = "true"
    while case == "true":
        dep = input("How much money would you like to deposit?\n")
        valid = 0
        counter = 0
        #For loop created to verifiy that each character in the user's input is a number or decimal and not anything else
        for char in dep:
            if(counter == 0 and char == '.'):
                print("Please put a number before a decimal.")
                valid = 0
                break
            if(char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9" or char == "0" or char == "."):
                valid = 1
            else:
                valid = 0
                break
            counter += 1
        if(valid == 0):
            print("Please use positive numbers only.")
            continue
        else:
            case = "false"
            dep = float(dep)
            balance += dep
            print("Please wait...")
            time.sleep(3)
            print("Done!\n")
            return(balance)

def view(balance):
    print("\nYour balance is: $",balance,"\n")

welcome()
while quit == "no":
    option = menu()
    if option == "exit":
        quit = exit()
    if option == "withdraw":
        balance = withdraw(balance)
    if option == "balance":
        view(balance)
    if option == "deposit":
        balance = deposit(balance)
    else:
        print("Please enter a valid option.")

print("Goodbye!")
