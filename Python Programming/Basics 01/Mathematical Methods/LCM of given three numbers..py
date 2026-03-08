# Write a program to print the LCM of given three numbers.
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value (n1).
#                      Second Line of Input Consists of One Integer Value (n2)
#             Third Line of Input Consists of One Integer Value (n3).
#
# Output        :- Print the LCM of given three values.
# Constraints  :-
#          'n1' Value is Must be Greater than zero or else Print "InvalId First Input".
#          'n2' Value is Must be Greater than zero or else Print "Invalid Second Input".
#          'n3' Value is Must be Greater than zero or else Print "InvaliD ThirD Input".
#         In the Given Three Inputs if any of two or three values are less than or equal to zero then Print "Sorry Invalid Inputs!".
# Example:
# Input 1  :      2
#                 5
#                 6
# Output 1:    30
n1=int(input("Enter Number:"))
n2=int(input("Enter number:"))
n3=int(input("Enter number:"))
mul=1
if (n1<=0 and n2<=0) or (n2<=0 and n3<=0) or (n3<=0 and n1<=0):
    print("Sorry Invalid Inputs!")
elif n1<=0:
    print("InvalId First Input")
elif n2<=0:
    print("Invalid Second Input")
elif n3<=0:
    print("InvaliD ThirD Input")
else:
    while(True):
        if mul%n1==0 and mul%n2==0 and mul%n3==0:
            print(mul)
            break
        mul+=1