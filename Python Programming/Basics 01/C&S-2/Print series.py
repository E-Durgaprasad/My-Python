"""Write a Program to Print the following series 2*3,3*4,4*5,......16*17
(Print in two ways – Pattern & Multiplied value) .
Constraints:
Input     :  Two Integer Values
Output  :  Print the Respective Pattern from the Given
            Number(First Number) to the Given Number(Second Number),
                    And
            Print the Respective Multiplied Value from
            the Given Number(First Number) to the Given Number(Second Number)
Example:.
Input 1    :    2
                16
Output 1 :    2*3, 3*4, 4*5, 5*6, 6*7, 7*8, 8*9, 9*10, 10*11, 11*12, 12*13, 13*14, 14*15, 15*16, 16*17
            6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272
"""
a, b = map(int, input("Enter Numbers:").split())
c = 0
s = 0
if a > b:
    a, b = b, a
for i in range(a, b + 1):
    c = c + 1
    if c != 1:
        print(", ", end="")
    print(f"{i}*{i + 1}", end="")
print()
for i in range(a, b + 1):
    s = s + 1
    if s != 1:
        print(", ", end="")
    print(i * (i + 1), end="")
