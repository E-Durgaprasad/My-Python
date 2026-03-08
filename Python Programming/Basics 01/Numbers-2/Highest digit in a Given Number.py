# Write a Program to print the Highest digit in a Given Number?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
# Output        :- Print Highest Digit in a Given Number.
# Constraints  :- Given Input is Must be Greater than Zero or else Print "Invalid Input.".
# Input 1  :    25696
# Output 1:    Highest Digit in a Given Number is 9.
n=int(input("Enter Number:"))
c=0
if n<=0:
    print("Invalid Input.")
else:
    while n>0:
        r=n%10
        if r>c:
            c=r
        n=n//10
    print(f"Highest Digit in a Given Number is {c}.")