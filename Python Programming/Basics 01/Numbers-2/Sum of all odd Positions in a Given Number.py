# Write a Program to Print The Sum of all odd Positions in a Given Number?
# Input          :- First Line of Input Consists of One Integer Value.
# Output        :- Print the Sum of Digits in Odd Positions.
# Constraints  :- Given Input Must be Greater than Zero or else Print "Invalid Input".
# Example:
# Input 1  :    5432
# Output 1:    6
n=int(input("Enter Number:"))
sum=0
c=0
if n<=0:
    print("Invalid Input")
else:
    while n>0:
        r=n%10
        c+=1
        n=n//10
        if c%2==1:
            sum=sum+r
    print(sum)