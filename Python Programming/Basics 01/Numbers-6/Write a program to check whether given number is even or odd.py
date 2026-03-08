# Description:
# Write a program to check whether Given Number is Even or Odd. (Without  % , / , + )
#
#
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
#
# Output        :- Print the Even or Odd.
#
# Constraints  :- Given Input is less than or equal to Zero then Print "InvaliD InpuT".
# Example:
# Input 1  :    9
#
# Output 1:    Odd

a=int(input("Enter Number:"))
if a<=0:
    print(" InvaliD InpuT")
else:
    if a & 1!=0:
        print("Odd")
    else:
        print("Even")