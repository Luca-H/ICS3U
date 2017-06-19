"""
Name: Luca Hudici
Filename: Employee Log Build 1.0
Purpose of program: To log employee work hours and pay.
Date: April 18 2017
"""
import math
import time
import random

input("Welcome to Employee Log Build 1.0! Press enter to continue...\n--------------------------------------------------------------\n")
overTimeRate = 1.5
maxHours = 80
workers = -1
workforce = []
employee = []
option = 0
exit = 0
#workers variable used to determine number of employees logged starting at 0
while(exit == 0):
    option = input("\nWhat do you want to do?\nType 'register' for a new entry.\nType 'view' to choose an entry to see.\nType 'exit' to exit the program.(All data gets wiped if program is exited.)\n")

    if(option == 'register'):
        workers += 1 #workers variable being used to log the number of employees starting at zero to provide options for user in the "view" section
        employee.append(input("\nEnter employee ID:\n"))
        employee.append(float(input("Enter payrate:\n")))
        employee.append(float(input("Enter hours worked:\n")))
        united = input("Do you want to pay $20 of your paycheque to United Way?\nType 'yes' or 'no':\n")
        if(united == 'yes'):
            employee.append(20)
        else:
            employee.append(0)
        if(employee[2] > maxHours):
            employee.append((maxHours*employee[1])+((employee[2]-maxHours)*(employee[1]*overTimeRate)))
        else:
            employee.append(employee[1]*employee[2])

        if(0 <= employee[4] < 96):
            employee.append(0)
        elif(480 >= employee[4] >= 96):
            employee.append(employee[4]*0.1)
        elif(1656 >= employee[4] > 480):
            employee.append((employee[4]*0.15)+38.4)
        elif(3877 >= employee[4] > 1656):
            employee.append((employee[4]*0.25)+214.8)
        elif(7983 >= employee[4] > 3877):
            employee.append((employee[4]*0.28)+770.05)
        elif(employee[4] > 7983):
            employee.append((employee[4]*0.33)+1919.73)
        else:
            print("You might have typed an invalid number.")
            continue
            del employee[:]

        employee.append(employee[4]-employee[3]-employee[5])
        print("\nEmployee ID:\n",employee[0],"\nPayrate:\n",employee[1],"\nHours worked:\n",employee[2],"\nUnited Way:\n",employee[3],"\nGross Pay:\n",employee[4],"\nTax Deductions:\n",employee[5],"\nNet Pay:\n",employee[6])
        (employee[0],"",employee[1],"\t\t",employee[2],"\t\t",employee[3],"\t\t",employee[4],"\t\t",employee[5])
        workforce.append(employee[:])
        del employee[:]
        time.sleep(1)

    if(option == 'view'):
        if(workers == -1):
            print("There are no logs.")
            continue
        print("\nPlease enter one of the following options: 0 -",workers,"\n NOTE: Entering a value that is not in the options above will crash the program!") #workers used to tell user log options to view
        choice = int(input())
        print("Employee ID:\n",workforce[choice][0],"\nPayrate:\n",workforce[choice][1],"\nHours worked:\n",workforce[choice][2],"\nUnited Way:\n",workforce[choice][3],"\nGross Pay:\n",workforce[choice][4],"\nTax Deductions:\n",workforce[choice][5],"\nNet Pay:\n",workforce[choice][6])
        time.sleep(1)

    if(option == 'exit'):
        certainty = input("\nAre you sure you want to exit? 'yes' or 'no'\n")
        if(certainty == 'yes'):
            break
        else:
            continue
            time.sleep(1)

print("\nThanks for using Employee Log!")
