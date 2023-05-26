#Write a Python program to check if a string is a palindrome.
str=input()
st=str
str=str[::-1]
if str == st:
    print("Pallindorome")
else:
    print("Not pallindrome")