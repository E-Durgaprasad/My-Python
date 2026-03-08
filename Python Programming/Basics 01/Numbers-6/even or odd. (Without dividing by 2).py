# Description:
# Write a program to check whether given number is even or odd. (Without dividing by 2)
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
# Output        :- Print the Given Number is Even or Odd.
# Constraints  :- Given Input is less than or equal to Zero then Print "Invalid Input".
# Example:
# Input 1  :    92
#
# Output 1:    Even
n=int(input("Enter numbre:"))
if n<=0:
    print("Invalid Input")
else:
    if (n & 1==0):
        print("Even")
    else:
        print("Odd")