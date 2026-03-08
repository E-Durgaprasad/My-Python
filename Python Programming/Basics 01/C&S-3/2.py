# Description:
# Write program to print the following series which is shown in Given Examples.
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
# Output        :- Print the Following Series.
# Constraints  :- No
# Input 1  :    25
# Output 1:     1, 3, divisible by five, 7, 9, 11, 13, divisible by five, 17, 19, 21, 23, divisible by five
n=int(input("Enter Numbers:"))
c=0
for i in range(n+1):
    if i%2==1:
        c=c+1
        if c!=1:
            print(", ",end="")
        if i%5==0:
            print("divisible by five",end="")
        else:
            print(i,end="")