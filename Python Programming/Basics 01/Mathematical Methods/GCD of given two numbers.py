# Write a program to print the GCD of given two numbers?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value (n1).
#                      Second Line of Input Consists of One Integer Value (n2).
# Output        :- Print the GCD of given two values.
# Constraints  :-
#             Both the values 'n1' & 'n2' must be Greater than zero or else Print "Invalid Inputs".
#
#            'n1' Value is Must be Greater than zero or else Print "Invalid First Input".
#
#              'n2' Value is Must be Greater than zero or else Print "Invalid Second Input.".
# Input 1  :    12
#             3
# Output 1:    3

n1=int(input("Enter number:"))
n2=int(input("Enter number:"))
min=n1 if n1<n2 else n2
fac=min
if n1<=0 and n2<=0:
    print("Invalid Inputs")
elif n1<=0:
    print("Invalid First Input")
elif n2<=0:
    print("Invalid Second Input.")
else:
    while (fac>=0):
        if n1%fac==0 and n2%fac==0:
            print(fac)
            break
        fac-=1