# Write a program to print the LCM of given two numbers
#
#
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value (n1).
#
#                      Second Line of Input Consists of One Integer Value (n2).
#
# Output        :- Print the LCM of given two values.
#
# Constraints  :-
#            Both the values 'n1' & 'n2' must be Greater than zero or else Print "Invalid Inputs.".
#             'n1' Value is Must be Greater than zero or else Print "Invalid First Input".
#
#           'n2' Value is Must be Greater than zero or else Print "InValid Second Input".
# Example:
# Input 1  :    2
#
#                   4
#
# Output 1:    4

n1=int(input())
n2=int(input())
max=1
mul=max
if n1<=0 and n2<=0:
    print("Invalid Inputs.")
elif n1<=0:
    print("Invalid First Input")
elif n2<=0:
    print("InValid Second Input")
else:
    while(True):
        if mul%n1==0 and mul%n2==0:
            print(mul)
            break
        mul=mul+max