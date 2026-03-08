# Write a program to find Factorial of a Given Number?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
# Output        :- Print the Factorial of a Given Number.
# Constraints  :- Given Inputs Must be Greater than or equal to Zero or else Print "Invalid InPut".
# Example:
# Input 1  :    6
# Output 1:    720
n=int(input("Enter Number:"))
if n<0:
    print("Invalid InPut")
else:
    sum=0
    fact=1
    for i in range(1,n+1):
        fact=i*fact
    print(fact)
