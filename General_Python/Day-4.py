#Write a program to find the maximum of three numbers.
a,b,c= map(int,input("Enter two numbers: ").split())
if a>b and a>c:
    print("a is greatest")
elif b>a and b>c:
    print("b is greatest")
else:
    print("c is greatest")
