# Description:
# Write a program to find Sum of all Palindrome Numbers between the Given Numbers?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
#                      Second Line of Input Consists of One Integer Value.
# Output        :- Print the Sum of All Palindromes Between the Given Numbers.
#
# Constraints  :- Either of the Given Inputs Must not equal to Zero or else Print "INVALID Inputs".
#                     If the starting value is greater than ending value, swap the values and continue the process.
#                      If there are no Palindrome values between the Given Numbers then Print "No Palindrome Values"
#                      If either input value is negative, convert all negative values to positive.
# Example:
# Input 1  :    100
#                   200
# Output 1:   1460
def pal(i):
    rev = 0
    t = i
    while t > 0:
        r = t % 10
        rev = rev * 10 + r
        t = t // 10
    return i == rev


n = int(input("Enter Number:"))
m = int(input("Enter Number:"))
if n == 0 or m == 0:
    print("INVALID Inputs")
else:
    if n < 0:
        n = abs(n)
    if m < 0:
        b = abs(m)
    if n > m:
        n, m = m, n
    s = 0
    for i in range(n + 1, m):
        if pal(i):
            s += i
    if s == 0:
        print("No Palindrome Values")
    else:
        print(s)
