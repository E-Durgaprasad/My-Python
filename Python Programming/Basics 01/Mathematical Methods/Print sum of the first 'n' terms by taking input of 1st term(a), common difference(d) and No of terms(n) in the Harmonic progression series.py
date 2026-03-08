# Write a Program to Print sum of the first 'n' terms by taking input of 1st term(a), common difference(d) and No of terms(n) in the Harmonic progression series?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value (1st Term (a)).
#                      Second Line of Input Consists of One Integer Value (Common Difference (d)).
#                      Third Line of Input Consists of One Integer Value (No of Terms (n)).
# Output        :- Print the sum of the Harmonic Progression Values.
# Constraints  :-
#                      'a' Value is an any Integer Value.
#                      'd' Value is an any Integer Value.
#                      'n' Value is Must be Greater than zero or else Print "Invalid Input.".
# Example:
# Input 1 :   1
#                 1
#                 6
# Output 1 : 2.45
a=int(input("Enter Number:"))
d=int(input("Enter Number:"))
n=int(input("Enter Number:"))
sum=0
c=0
ap=0
if n<0:
    print("Invalid Input.")
else:
    for i in range(0,n):
        ap=a+i*d
        sum=sum+1/ap
    print(f"{sum:.2f}")
