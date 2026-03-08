# Write a Program to check if the Given Number is Perfect Square or Not a perfect Square?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
# Output        :- Print Given Number is Perfect Square or Not.
# Constraints  :- Given Input is a Zero or a Negative Value then Print "InvaliD Input"
# Example:
# Input 1  :    10
# Output 1:    Given Number is Not a Perfect Square.
n=int(input("Enter Number:"))
if n<=0:
    print("InvaliD Input")
else:
    for i in range(1,n):
        r=i*i
        if r==n:
            print("Given Number is a Perfect Square.")
            break
    else:
        print("Given Number is Not a Perfect Square.")