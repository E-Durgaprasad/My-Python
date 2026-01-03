"""Description:
Write a Program to Print the Following Pattern?
If Input is 6 then Print
1
1 2
1 2 3
1 2 3 5
1 2 3 5 8
1 2 3 5 8 13"""
n = int(input("Enter number: "))
for i in range(1,n+1):
    a,b=1,2
    for j in range(1, i + 1):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
    print()