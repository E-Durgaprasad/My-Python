"""Description:
Write a Program to Print the Following Pattern?
If Input is 3 then Print
12321
 232
  3  """
n = int(input("Enter the number: "))
for i in range(1, n + 1):
    c = n
    t = i
    for j in range(1, i):
        print("", end=" ")
    for k in range(1, n - i + 1):
        print(t, end="")
        t = t + 1
    for l in range(1, n - i + 2):
        print(c, end="")
        c = c - 1
    print()