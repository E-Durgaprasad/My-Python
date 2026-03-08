# Find and Print the
#  term value in the Arithmetic progression series by taking input of 1st term(a), common difference(d) and
#  term ?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value (1st Term (a))
#         Second Line of Input Consists of One Integer Value (Common Difference (d)).
#                      Third Line of Input Consists of One Integer Value (No of Terms (n)).
# Output        :- Print the
#  term value of Arithmetic Progression Values.
# Constraints  :-
#         'a' Value is an any Integer Value.
#      'd' Value is an any Integer Value.
#        'n' Value is Must be Greater than zero or else Print "InValid Input".
# Input 1  :  2
#           4
#            8
# Output 1:    Last term value is : 30.
a=int(input("Enter NUmber:"))
d=int(input("Enter NUmber:"))
n=int(input("Enter NUmber:"))
c=0
if n<0:
    print("InValid Input.")
else:
    for i in range(n):
        c+=1
        if c==1:
            print("Last term value is : ",end="")
    print(f"{a+(n-1)*d}.")