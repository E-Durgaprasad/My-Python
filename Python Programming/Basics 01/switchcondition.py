"""Write a program to perform Addition,
Subtraction, Multiplication and Division of 2 Numbers
based on the user
inputs by using Switch condition.(+ , - , * , /, %)."""
a=int(input("Enter value: "))
b=int(input("Enter value: "))
c=input("Enter operator:")
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
elif c=="%":
    print(a%b)