# Write a Program to Check if The given year is Leap Year or not?
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
# Output        :- Print the "Leap Year." or "Not a Leap Year.".
# Constraints  :- Given Input Must be Greater than Zero or else Print "Given Year is Invalid Input.".
# Input 1  :    1983
# Output 1:    Not a Leap Year.
y=int(input("Enter year:"))
if y<=0:
    print("Given Year is Invalid Input.")
else:
    if (y%100==0 and y%400==0) or (y%4==0 and y%100!=0):
        print("Leap Year.")
    else:
        print("Not a Leap Year.")