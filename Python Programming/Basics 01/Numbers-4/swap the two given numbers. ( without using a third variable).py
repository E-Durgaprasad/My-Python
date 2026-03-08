# Write a program to swap the two given numbers. ( without using a third variable)
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
#                      Second Line of Input Consists of One Integer Value.
# Output        :- Print the Given 2 Numbers after Swapping.
# input 1  :    210
#                   208
# Output 1:    208
#             210
a=int(input("Enter Number:"))
b=int(input("Enter Number:"))
a,b=b,a
print(a)
print(b)