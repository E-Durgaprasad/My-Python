# Description:
# Write program to print the following series which is shown in Given Examples
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
# Output        :- Print the Following Series.
# Constraints  :- Given Input Must be Greater than Zero or else Print Invalid Input.
# Input
# 1: 10
# Output
# 1: 5, 10, 5, 10, 5, 10, 5, 10, 5, 10

n=int(input("Enter Numbers:"))
c=0
if n>0:
    for i in range(n):
        c=c+1
        if c!=1:
            print(", ",end="")
        if i%2==0:
            print(5 ,end="")
        else:
            print(10 ,end="")
else:
    print("Invalid Input")

