# Write a program to print the GCD of given three numbers?
# Constraints
# Input          :- First Line of Input Consists of One Integer Value (n1).
#                      Second Line of Input Consists of One Integer Value (n2).
#                      Third Line of Input Consists of One Integer Value (n3).
# Output        :- Print the GCD of given three values.
# Constraints  :-
#                      'n1' Value is Must be Greater than zero or else Print "Invalid First Input".
#                      'n2' Value is Must be Greater than zero or else Print "Invalid Second Input".
#                      'n3' Value is Must be Greater than zero or else Print "Invalid Third Input".
#                      In the Given Three Inputs if any of two or three values are less than or Equal to zero then Print "Invalid Inputs"
# Input 1  :    24
#
#                   34
#
#                   44
#
# Output 1:    2
n1=int(input("Enter Number:"))
n2=int(input("Enter Number:"))
n3=int(input("Enter Number:"))
m=max(n1,n2,n3)
fact=m
if (n1<=0 and n2<=0) or (n2<=0 and n3<=0) or (n3<=0 and n1<=0):
    print("Invalid Inputs")
elif n1<=0:
    print("Invalid First Input")
elif n2<=0:
    print("Invalid Second Input")
elif n3<=0:
    print("Invalid Third Input")
else:
    while fact>=0:
        if n1%fact==0 and n2%fact==0 and n3%fact==0:
            print(fact)
            break
        fact-=1