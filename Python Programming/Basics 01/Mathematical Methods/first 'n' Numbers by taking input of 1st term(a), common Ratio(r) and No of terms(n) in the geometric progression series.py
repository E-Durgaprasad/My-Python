# Write a Program to Print first 'n' Numbers by taking input of 1st term(a), common Ratio(r) and No of terms(n) in the geometric progression series ?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value (1st Term (a)).
#                      Second Line of Input Consists of One Integer Value (Common Ratio (r)
#                      Third Line of Input Consists of One Integer Value (No of Terms (n)).
# Output        :- Print the Geometric Progression Values.
# Constraints  :
#                      'a' Value is an any Integer Value.
#                      'r' Value is an any Integer Value.
#                      'n' Value is Must be Greater than zero or else Print "Invalid Input".
# Example:
# Input 1  :    2
#                   4
#                   8
# Output 1:    2, 8, 32, 128, 512, 2048, 8192, 32768.
a=int(input("Enter Number:"))
r=int(input("Enter Number:"))
n=int(input("Enter Number:"))
c=0
if n<0:
    print("Invalid Input.")
else:
    for i in range(n):
        c+=1
        if c!=1:
            print(", ",end="")
        print(a,end="")
        a=a*r
    print(".")