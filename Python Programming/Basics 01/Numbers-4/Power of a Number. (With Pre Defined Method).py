# Write a program to Calculate Power of a Number. (With Pre Defined Method)
#
#
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value ( Base Value ).
#
#                      Second Line of Input Consists of One Integer Value ( Exponent Value ).
#
# Output        :- Print the Power Value.
#
# Constraints  :- Given Inputs is Must be Greater than Zero or else Print "Invalid Inputs".
# Input 1  :    2
#            5
# Output 1:    2 Power 5 value is 32.

a = int(input("Enter Number:"))
b = int(input("Enter Number:"))
if a <= 0 or b <= 0:
    print("Invalid Inputs")
else:
    if a > 0 and b > 0:
        r = a ** b
    print(f"{a} Power {b} value is {r}.")
