# Write program to print the following series which is shown in Given Examples.
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
#                      Second Line of Input Consists of One Integer Value.
# Output        :- Print the Following Series.
# Constraints  :- Given Inputs Must be Greater than Zero or else Print "Invalid Inputs".
# Input 1  :    10
#
#                   31
#
# Output 1:    10^2, 12^2, 14^2, 16^2, 18^2, 20^2, 22^2, 24^2, 26^2, 28^2, 30^2

n=int(input("Enter Number:"))
m=int(input("Enter Number:"))
c=0
if n<=0 or m<=0:
    print("Invalid Inputs")
else:
    for i in range(n,m+1,2):
        c+=1
        if c!=1:
            print(", ",end="")
        print(f"{i}^2",end="")