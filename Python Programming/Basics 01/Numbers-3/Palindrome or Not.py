"""Write a program to check Given Number is Palindrome or Not
Input          :- First Line of Input Consists of One Integer Value.
Output        :- If Given Number is a Palindrome then, print "Palindrome" or else print, "Not a Palindrome".

Example:
Input 1  :    1698
Output 1:    Not a Palindrome
"""
n=int(input("Enter Number:"))
rev=0
temp=n
while n > 0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10
if temp == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")