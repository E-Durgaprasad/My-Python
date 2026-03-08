# Description:
# Write a program to print following pattern
#
# if input is 10 and -5
# output will be 10@9,9@8,8@7,7@6,6@5,5@4,4@3,3@2,2@1,1@0,0@-1,-1@-2,-2@-3,-3@-4,-4@-5,-5@-6
# Constraints:
# Input :          First line of input contains integer denotes starting range
#                      Second line of input contains integer denotes ending range
#  Input :            10
#                         -5
# Output :         10@9,9@8,8@7,7@6,6@5,5@4,4@3,3@2,2@1,1@0,0@-1,-1@-2,-2@-3,-3@-4,-4@-5,-5@-6
n = int(input("Enter Number:"))
m = int(input("Enter Number:"))
if n > m:
    c = 0
    for i in range(n, m - 1, -1):
        c += 1
        if c != 1:
            print(",", end="")
        if i >= 0:
            print(f"{i}@{i - 1}", end="")
        else:
            print(f"{i}@{i - 1}", end="")
else:
    c = 0
    for i in range(n, m + 1, 1):
        c += 1
        if c != 1:
            print(",", end="")
        if i > 0:
            print(f"{i}@{i + 1}", end="")
        else:
            print(f"{i}@{i + 1}", end="")
