# Write a Program to Print The Sum of the Even Digits in a Given Number?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
# Output        :- Print the Sum of the Even Digits.
# Constraints  :- Given Input Must be Greater than Zero or else Print "Invalid Input".
# Example:
# Input 1  :    212
# Output 1:    4
n=int(input("Enter Number:"))
sum=0
if n<=0:
    print("Invalid Input")
else:
    while n>0:
        r=n%10
        if r%2==0:
            sum=sum+r
        n=n//10
    print(sum)