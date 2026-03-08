# Write a program to check if the Given Number is Armstrong or not?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
#
# Output        :- Print the Armstrong Number or Not a Armstrong Number.
#
# Constraints  :- Given Input is Must be Greater than Zero or else Print "Invalid Input".
# Input 1  :    253
# Output 1:    Not a Armstrong Number
n=int(input("Enter Number:"))
if n<=0:
    print("Invalid Input")
else:
    sum,t=0,n
    while t>0:
        r=t%10
        sum+=r**3
        t=t//10
    if n==sum:
        print("Armstrong Number")
    else:
        print("Not a Armstrong Number")