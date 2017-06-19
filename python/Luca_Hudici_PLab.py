"""
Name: Luca Hudici
Filename: Jump Calculator 60
Purpose of program: To determine the height of a jump
Date: March 1 2017
"""
import math
print("Welcome, to the Jump Calculator 60; because the gravity constant is 60.")
GravFactor = int(60)
IniSpeed = float(input("Please enter an initial speed:"))
PowerFactor = float(input("Please enter a power factor:"))
JumpSpeed = IniSpeed * PowerFactor
JumpSpeed *= JumpSpeed
Height = JumpSpeed/GravFactor
print("Your height is",Height,"dots.")
