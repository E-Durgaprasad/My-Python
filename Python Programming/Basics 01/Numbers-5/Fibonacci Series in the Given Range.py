# Description:
# Write a program to print Fibonacci Series in the Given Range.
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
#                      Second Line of Input Consists of One Integer Value.
# Output        :- Print the Fibonacci Series in the Given Range.
# Constraints  :- Given Inputs Must be Greater than or equal to Zero or else Print "Invalid Inputs".
#           If there are no Fibonacci Series values in the Given Range then, Print "No Fibonacci Series Values".
# input 1  :    13
#
#                   91
#
# Output 1:    13 21 34 55 89
n=int(input("Enter Number:"))
m=int(input("Enter Number:"))
a,b=0,1
count=0
if n<0 or m<0:
    print("Invalid Inputs")
# elif n<0 or m<0:
#     print("Invalid Inputs")
else:
    if n>m:
        n,m=m,n
    while a<=m:
        if a>=n:
            count+=1
            print(a,end=" ")
        c=a+b
        a=b
        b=c
    if count==0:
        print("No Fibonacci Series Values",end="")