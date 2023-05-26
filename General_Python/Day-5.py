#Write a program to swap the values of two variables.
a,b =map(int,input("Enter two numbers: ").split())
print(f"Before swapping values of a and b is {a} and {b}")
a,b=b,a
print(f"After swapping values of a and b is {a} and {b}")