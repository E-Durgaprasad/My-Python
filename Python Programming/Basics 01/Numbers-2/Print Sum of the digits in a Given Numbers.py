# Write a Program to Print Sum of the digits in a Given Number
# Input          :- First Line of Input Consists of One Integer Value.
# Output        :- Print the Sum of Digits.
# Constraints  :- Given Input Must be Greater than Zero or else Print Invalid Input.
# Example:
# Input 1  :    210
# Output 1:    3
n=int(input("Enter Number:"))
sum=0
if n<=0:
    print("Invalid Input")
else:
    while n>0:
        r=n%10
        sum=sum+r
        n=n//10
    print(sum)