"""Write a Program to Print the Biggest Number out of
the Given three Numbers?"""

a,b,c=map(int,input("Enter Numbers:").split())
if a>b and a>c:
    biggest=a
elif b>a and b>c:
    biggest=b
elif c>a and c>b:
    biggest=c
print(biggest,"is a Biggest Number from the Given Numbers")