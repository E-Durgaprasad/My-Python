# Description:
# Write a program to find Average of all Palindrome Numbers in the Range?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
#                      Second Line of Input Consists of One Integer Value.
# Output        :- Print the Average of All Palindromes In the Given Range.
# Constraints  :- Either of the Given Inputs Must not equal to Zero or else Print "INVALID Inputs".
#                      If there are no Palindrome values in the Given Range then, Print "No Palindrome Values".
#                      If Either of the Given Inputs is Negative then convert all the Negative Values to Positive Values.
#                      If the First Input is Greater then Second Input then, Print "Given Inputs are Swapped".
# Example:
# Input
# 1: 100
# 120
# Output
# 106.00
#
a = int(input("Enter Number:"))
b = int(input("Enter Number:"))


def pal(i):
    rev = 0
    t = i
    while t > 0:
        r = t % 10
        rev = rev * 10 + r
        t = t // 10
    return i == rev


if a == 0 or b == 0:
    print("INVALID Inputs")
else:
    if a <= 0:
        a = abs(a)
    if b <= 0:
        b = abs(b)
    if a >= b:
        print("Given Inputs are Swapped")
    else:
        c = 0
        sum = 0
        for i in range(a, b + 1):
            if pal(i):
                c = c + 1
                sum = sum + i
        if c == 0:
            print("No Palindrome Values")
        else:
            avg = sum / c
            print(f"{avg:.2f}")

