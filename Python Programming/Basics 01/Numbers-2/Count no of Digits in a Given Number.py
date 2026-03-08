# Write a Program to Print Count no of Digits in a Given Number?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
# Output        :- Print Integer Number ( No of Digits in Given Number ).
# Constraints  :- Given Input is Zero then Print "InvaliD Input".
# Example:
# Input 1  :    418
# Output 1:    Given Number consists of 3 Digits.
n=int(input("Enter Number:"))
c=0
temp=n
if n==0:
    print("InvaliD Input")
else:
    if n<0:
        n=n*-1
    while n>0:
        r=n%10
        c+=1
        n=n//10
    if c==1:
        if temp<0:
            print(f"Given Number consists of only {c} Digit and it is Negative Value.")
        else:
            print(f"Given Number consists of only {c} Digit.")
    elif c>=2:
        if temp<0:
            print(f"Given Number consists of {c} Digits and it is Negative Value.")
        else:
            print(f"Given Number consists of {c} Digits.")