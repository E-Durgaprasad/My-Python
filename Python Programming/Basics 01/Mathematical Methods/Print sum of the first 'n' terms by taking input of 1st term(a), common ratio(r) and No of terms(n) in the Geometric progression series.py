# Write a Program to Print sum of the first 'n' terms by taking input of 1st term(a), common ratio(r) and No of terms(n) in the Geometric progression series?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value (1st Term (a)).
#                      Second Line of Input Consists of One Integer Value (Common Ratio (r)).
#                      Third Line of Input Consists of One Integer Value (No of Terms (n)).
# Output        :- Print Sum of the Geometric Progression Values.
# Constraints  :-
#                      'a' Value is an any Integer Value.
#                      'r' Value is an any Integer Value.
#                      'n' Value is Must be Greater than zero or else Print "Invalid Input".
# Example:
# Input 1  :    2
#                   4
#                   8
# Output 1:    43690
a=int(input("Enter Number:"))
r=int(input("Enter Number:"))
n=int(input("Enter Number:"))
sum=0
if n<0:
    print("Invalid Input")
else:
    for i in range(n):
        sum=sum+a
        a=a*r
    print(sum)