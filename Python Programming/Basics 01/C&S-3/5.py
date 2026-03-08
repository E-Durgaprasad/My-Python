# Write program to print the following series which is shown in Given Examples.
# Constraints:
# Input         :-   First Line Of Input consists of One Integer value.
#                       Second Line Of Input consists of One Integer value.
# Output       :-   Print the Following Series.
# Constraints :-   All the Values Should be Greater than Zero or else print "Invalid Inputs".
# Input 1   : 100
#             1000
# Output 1 : 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000
n=int(input("Enter Number:"))
m=int(input("Enter Number"))
c=0
if n<=0 or m<=0:
    print("Invalid Inputs")
else:
    for i in range(n,m+1,100):
        c=c+1
        if c!=1:
            print(", ",end="")
        print(i, end="")