# Description:
# Write program to print the following series which is shown in Given Examples.
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
# Output        :- Print the Following Series.
# Input 1  :    36
#
# Output 1:    1, even, 3, even, 5, even, 7, even, 9, even, 11, even, 13, even, 15, even, 17, even, 19, even, 21, even, 23, even, 25, even, 27, even, 29, even, 31, even, 33, even, 35, even
n=int(input("Enter Number:"))
c=0
for i in range(1,n+1):
    if i%2==0:
        c=+1
        if c!=0:
            print(", ",end="")
        print("even",end="")
    else:
        if i !=1:
            print(", ", end="")
        print(i,end="")