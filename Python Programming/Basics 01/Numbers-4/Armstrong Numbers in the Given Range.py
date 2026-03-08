# Write a program to print the Armstrong Numbers in the Given Range.
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
#                      Second Line of Input Consists of One Integer Value.
# Output        :- Print the All Armstrong Numbers.
#
# Constraints  :- Given Inputs is Must be Greater than Zero or else Print "Invalid Inputs".
#       If there are No Armstrong Numbers Between the Given Range then print, "No Armstrong Numbers".
#        If starting range is greater than ending range, swap both the values and print the armstrong numbers.
# Input 1  :    1
#           200
# Output 1:Armstrong Numbers in the Given Range is 1, 2, 3, 4, 5, 6, 7, 8, 9, 153.
def arm(i):
    t, dc = i, 0
    while t > 0:
        r = t % 10
        dc += 1
        t = t // 10
    sum, t = 0, i
    while t > 0:
        r = t % 10
        sum = sum + r ** dc
        t = t // 10
    return sum == i


a = int(input("Enter Number:"))
b = int(input("Enter Number:"))
if a == 0 or b == 0:
    print("Invalid Inputs")
elif a < 0:
    print("Invalid Inputs")
else:
    count = 0
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        if arm(i):
            count += 1
            if count == 1:
                print("Armstrong Numbers in the Given Range is ", end="")
            if count != 1:
                print(", ", end="")
            print(i, end="")
    if count == 0:
        print("No Armstrong Numbers")
    else:
        print(".")
