# Write a program to print the Sum of the Fibonacci Series of first N terms.
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
# Output        :- Print the Sum of the First N terms of Fibonacci Series.
# Constraints  :- Given Input is Must be Greater than Zero or else Print "Invalid Input".
# Example:
# Input 1  :    10
# Output 1:    88
n=int(input("Enter Number: "))
if n<=0:
    print("Invalid Input")
else:
    a,b=0,1
    sum=0
    for i in range(1,n+1):
        sum=sum+a
        c=a+b
        a=b
        b=c
    print(sum)