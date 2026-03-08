# Find the nth term value in the geometric progression series by taking input of 1st term(a), common Ratio(r) and nth term ?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value (1st Term (a)).
#                      Second Line of Input Consists of One Integer Value (Common Ratio (r)).
#                      Third Line of Input Consists of One Integer Value (No of Terms (n)).
# Output        :- Print the nth term value of Geomentric Progression Values.
# Constraints  :-
#                      'a' Value is an any Integer Value.
#                      'r' Value is an any Integer Value.
#                      'n' Value is Must be Greater than zero or else Print "InValid Input".
# Input 1  :    2
#                   4
#                   8
# Output 1:    Last term value is : 32768
a=int(input("Enter Number:"))
r=int(input("Enter Number:"))
n=int(input("Enter Number:"))
c=0
if n<0:
    print("InValid Input.")
else:
    for i in range(n):
        c+=1
        if c==1:
            print(" Last term value is : ",end="")
    print(f"{a*(r**(n-1))}.")