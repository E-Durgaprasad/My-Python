# Write a program to Print the Reverse of a Given Number?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
# Output        :- Print the Reverse of a Given Number.
# Constraints  :- Given Input Must be Greater than Zero or else Print, "InValid Input".
# Input 1  :    1698
# Output 1:    8961
n=int(input("Enter Number:"))
if n<=0:
    print("InValid Input")
else:
    i=0
    while n>0:
        r=n%10
        i=i*10+r
        n=n//10
    print(i)