# Description:
# Write A Program to check the Given Number is Perfect Square or not?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
# Output        :- Print the Given Number is Perfect Square or not Perfect Square.
#
# Constraints  :-  If the given input is negative convert it into positive
# If the Given Input is equal to Zero then Print "Invalid Input"
# Example:
# Input
# 1: 9
# Output
# 1: Given
# Number is Perfect
# Square.
import math
n=int(input("Enter Number:"))
if n==0:
    print("Invalid Input.")
elif n<0:
    print("Given Number is Not a Perfect Square.")
else:
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            print("Given Number is Perfect Square.")
            break
    else:
        print("Given Number is Not a Perfect Square.")