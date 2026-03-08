# Write program to print the following series which is shown in Given Examples.
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
#                      Second Line of Input Consists of One Integer Value.
# Output        :- Print the Following Series.
# Example:
# Input 1  :    10
#                   -12
# Output 1:
# 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, (-5), (-10), (-15), (-20), (-25), (-30), (-35), (-40), (-45), (-50), (-55), (-60)
n=int(input("Enter Number:"))
m=int(input("Enter Number:"))
if n>m:
    c=0
    for i in range(n,m-1,-1):
        c+=1
        if c!=1:
            print(", ",end="")
        if i>=0:
            print(f"{i*5}",end="")
        else:
            print(f"({i*5})",end="")
else:
    c=0
    for i in range(n,m+1,1):
        c+=1
        if c!=1:
            print(", ",end="")
        if i>=0:
            print(f"{i*5}",end="")
        else:
            print(f"({i*5})",end="")