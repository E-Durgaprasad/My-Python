# Write a Program to Print first 'n' Numbers by taking input of
#  term(a), common difference(d) and no of terms(n) in the Arithmetic progression series?
# Constraints:
# Input        :- First Line of Input Consists of One Integer Value (
#  Term (a)).
#                      Second Line of Input Consists of One Integer Value (Common Difference (d)).
#                      Third Line of Input Consists of One Integer Value (No of Terms (n)).
# Output        :- Print the Arithmetic Progression Values.
# Constraints  :-
#          'a' Value is an any Integer Value.
#          'd' Value is an any Integer Value.
#         'n' Value is Must be Greater than zero or else Print "Invalid Input".
# Input 1  :    2
#          4
#            8
# Output 1:    2, 6, 10, 14, 18, 22, 26, 30.
a=int(input("Enter Number:"))
d=int(input("Enter Number:"))
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
        a=a+d
    print(".")
