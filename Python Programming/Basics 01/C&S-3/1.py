# Description:
# Write program to print the following series which is shown in Given Examples.
# Constraints:
# Input          :- First Line of Input Consists of One float Value.
#                      Second Line of Input Consists of One float Value.
# Output        :- Print the Following Series.
# Constraints  :- NoInput 1  :    10.7
#                   12.1
# Output 1:
# 10.7^2, 10.9^2, 11.1^2,11.3^2, 11.5^2, 11.7^2, 11.9^2, 12.1^2.
n = float(input("Enter Number:"))
m = float(input("Enter NUmber:"))
c = 0
for i in range(int(n * 10), int(m * 10) + 1, 2):
    a = i / 10
    c += 1
    if c != 1:
        print(", ", end="")
    print(f"{a:.1f}^2", end="")
print(".")
