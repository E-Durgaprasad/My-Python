# Write a program to the check if the Given Number is a Palindrome or not and if it is a palindrome then Print PALINDROME, else Print the Reverse Value of a Given Number ?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
# Output        :- Print the Palindrome or Reverse value.
# Constraints  :- Given Input is Must be Greater than or equal to Zero or else Print "Invalid Input".
#                      If the Given Number is Zero then Print "Zero".
# Input 1  :    1698
#
# Output 1:    Reverse of a Given Number is 8961
n=int(input("Enter Number:"))
if n<0:
    print("Invalid Input")
elif n==0:
    print("Zero")
else:
    s=0
    t=n
    while t>0:
        r=t%10
        s=s*10+r
        t=t//10
    if s==n:
        print("Given Number is Palindrome")
    else:
        print(f"Reverse of a Given Number is {s}")