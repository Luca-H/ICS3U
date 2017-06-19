"""
Name: Luca Hudici
Filename: Marks calculator
Purpose of program: To determine students' marks and the class average
Date: 4/4/17
"""
import math
import time
import random

input("Welcome to mark calculator, press next to continue...")
total_marks = 0
students = 0
grade_level = "0"
while(1):
    #While statement used to allow for multiple students to be entered
    studentID = input("Please enter a student ID:\n")
    term_mark = float(input("Please enter the student's term mark:\n"))
    summative1 = float(input("Please enter the student's summative mark:\n"))
    summative2 = float(input("Please enter the student's exam or summative 2 mark:\n"))
    if((0 < term_mark > 100) or (0 < summative1 > 100) or (0 < summative2 > 100)):
        print("You have entered an invalid mark somewhere, please try again.")
        continue
    final_mark = (term_mark * 0.7) + (summative1 * 0.2) + (summative2 * 0.1)
    total_marks += final_mark
    students += 1
    if(0 <= final_mark <= 49):
        grade_level = 'R'
    elif(50 <= final_mark < 53):
        grade_level = '1-'
    elif(53 <= final_mark < 57):
        grade_level = '1'
    elif(57 <= final_mark < 60):
        grade_level = "1+"
    elif(60 <= final_mark < 63):
        grade_level = '2-'
    elif(63 <= final_mark < 67):
        grade_level = '2'
    elif(67 <= final_mark < 70):
        grade_level = '2+'
    elif(70 <= final_mark < 73):
        grade_level = '3-'
    elif(73 <= final_mark < 77):
        grade_level = '3'
    elif(77 <= final_mark < 80):
        grade_level = '3+'
    elif(80 <= final_mark < 87):
        grade_level = '4-'
    elif(87 <= final_mark < 95):
        grade_level = '4'
    elif(95 <= final_mark < 100):
        grade_level = '4+'
    elif(final_mark == 100):
        grade_level = '4++'
    #If else block used for grade level *Fixed range gaps that would have resulted in innapropriate Level R bug
    print("\n",studentID,"\nFinal mark:",final_mark,"\nGrade level:",grade_level)

    option = input("Do you want to enter another student? Press y for yes and n for no.\n")
    if(option == 'n'):
        break
#break statement used for "no" option
class_average = total_marks / students

print("The class average is:",class_average)
