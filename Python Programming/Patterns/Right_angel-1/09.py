"""Description:
Write a Program to Print the Following Pattern?
If Input is 4 then Print
A
B C
D E F
G H I J"""

n = int(input("Enter Number:"))
if n < 0:
    n = abs(n)
if n == 0:
    print("Invalid Input")
elif n >= 1 and n <= 6:
    c = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(chr(64 + c), end=" ")
            c += 1
        print()
else:
    print("Range Exceeded")