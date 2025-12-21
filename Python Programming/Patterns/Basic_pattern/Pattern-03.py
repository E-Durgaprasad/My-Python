"""Write a Program to Print the following Basic Pattern?
If Input is 5 then Print
1 0 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 0 1

Input 2  : 6
Output 2:
1 0 1 0 1 0
0 1 0 1 0 1
1 0 1 0 1 0
0 1 0 1 0 1
1 0 1 0 1 0
0 1 0 1 0 1
"""
n = int(input("Enter a number:"))
if n <= 0:
    print("Invalid Input")
else:
    if n % 2 == 1:
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if j % 2 == 0:
                    print("0", end=" ")
                else:
                    print("1", end=" ")
            print()

    else:
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i % 2 == 1:
                    if j % 2 == 1:
                        print(1, end=" ")
                    else:
                        print(0, end=" ")
                else:
                    if j % 2 == 1:
                        print(0, end=" ")
                    else:
                        print(1, end=" ")
            print()