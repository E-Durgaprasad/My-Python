# Write a Program to Print first 'n' Numbers by taking input of 1st term(a), common difference(d) and no of terms(n) in the Harmonic progression series?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value (1st Term (a)
#                      Second Line of Input Consists of One Integer Value (Common Difference (d)).
#
#                      Third Line of Input Consists of One Integer Value (No of Terms (n)).
# Output        :- Print the Harmonic Progression Values.
# Constraints  :-
#        'a' Value is an any Integer Value.
#          'd' Value is an any Integer Value.
#          'n' Value is Must be Greater than zero or else Print "Invalid Input".
# Example:
# Input 1 :   1
#                 1
#                 6
# Output 1 : 1.00, 0.50, 0.33, 0.25, 0.20, 0.17
a=int(input("Enter NUmber:"))
b=int(input("Enter NUmber:"))
n=int(input("Enter NUmber:"))
ap=0
c=0
d=0
if n<=0:
    print("Invalid Input")
else:
    for i in range(0,n):
        c=c+1
        ap=a+i*b
        if c!=1:
            print(",",end=" ")
        print(f"{1/ap:.2f}",end="")