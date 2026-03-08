# Write a Program to Print sum of the first 'n' terms by taking input of 1st term(a), common difference(d) and No of terms(n) in the Arithmetic progression series?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value (1st Term (a)).
#                      Second Line of Input Consists of One Integer Value (Common Difference (d)).
#                      Third Line of Input Consists of One Integer Value (No of Terms (n)).
# Output        :- Print Sum of the Arithmetic Progression Values.
#
# Constraints  :-
#                 'a' Value is an any Integer Value.
#              'd' Value is an any Integer Value.
#             'n' Value is Must be Greater than zero or else Print "Invalid input".
# input 1  :    2
#
#                   4
#
#                   8
#
# Output 1:    2 + 6 + 10 + 14 + 18 + 22 + 26 + 30 = 128.
a=int(input("Enter number:"))
d=int(input("Enter number:"))
n=int(input("Enter number:"))
sum=0
c=0
if n<0:
    print("Invalid input.")
else:
    for i in range(n):
        c+=1
        if c!=1:
            print(" + ",end="")
        sum=sum+a
        print(a,end="")
        a=a+d
    print(f" = {sum}.",end="")