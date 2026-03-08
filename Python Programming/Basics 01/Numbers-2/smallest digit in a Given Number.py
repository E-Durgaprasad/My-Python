# Write a Program to print the smallest digit in a Given Number?
# Input          :- First Line of Input Consists of One Integer Value.
# Output        :- Print Smallest Digit in a Given Number.
# Constraints  :- Given Input is Must be Greater than Zero or else Print "Invalid Input.".
# Example:
# Input 1  :    25696
# Output 1:    Smallest Digit in a Given Number is 2.

n=int(input("Enter number:"))
if n<0:
    print("Invalid Input.")
else:
    min=9
    while n>0:
        r=n%10
        if min>r:
            min=r
        n=n//10
    print(f"Smallest Digit in a Given Number is {min}.")
