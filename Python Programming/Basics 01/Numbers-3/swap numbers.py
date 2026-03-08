# Description:
# Write a program to swap the two given numbers.
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
#                      Second Line of Input Consists of One Integer Value.
# Output        :- Print the Two Numbers after Swapping.
# Example:
# Input 1  :    210
#             208
# Output 1:    208
#           210
n=int(input("Enter Number:"))
m=int(input("Enter Number:"))
t=n
n=m
m=t
print(n)
print(m)