"""Write a Program to Print the Following Pattern?
If Input is 5 then Print
%  % % % %
& & & &
% % %
& &
%"""
n = int(input("Enter no. of elements: "))
for i in range(1,n+1):
    for j in range(1,n-i+2):
        if i%2==0:
            print(f"&",end=" ")
        else:
            print(f"%",end=" ")
    print()
