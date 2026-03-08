# Write a program to Count the Number of digits in a Given Number?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
#
# Output        :- Print the Count of Digits in a Given Number.
#
# Constraints  :- Given Input Must be Greater than Ten or else Print "Invalid Input".
# Input 1  :    25
#
# Output 1:    2
a=int(input("Enter NUmber:"))
if a<=10:
    print("Invalid Input")
else:
    c=0
    while a>0:
        r=a%10
        c+=1
        a=a//10
    print(c)