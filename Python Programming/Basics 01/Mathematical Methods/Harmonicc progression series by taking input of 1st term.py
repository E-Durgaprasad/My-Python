# Find the nth term value in the Harmonic progression series by taking input of 1st term(a), common difference(d) and nth term ?
#
#
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value (1st Term (a)).
#
#                      Second Line of Input Consists of One Integer Value (Common Difference (d)).
#
#                      Third Line of Input Consists of One Integer Value (No of Terms (n)).
#
# Output        :- Print the nth term value of Harmonic Progression Values.
#
# Constraints  :-
#
#                      'a' Value is an any Integer Value.
#
#                      'd' Value is an any Integer Value.
#
#                      'n' Value is Must be Greater than zero or else Print "InvaliD InPut"
# .Example:
# Input 1 :   1
#
#                 1
#
#                 6
#
# Output 1 : 0.17

a=int(input("Enter Numbers:"))
d=int(input("Enter Numbers:"))
n=int(input("Enter Numbers:"))
ap=0
c=0
if n<0:
    print("InvaliD InPut")
else:
    for i in range(n):
        ap=a+i*d
    print(f"{1/ap:.2f}",end="")