#Write a Python program to find the sum of all the numbers in a list.
lst=[]
sum=0
n=int(input("Enter the size of list:"))
for i in range(0,n):
    ele = input()
    lst.append(ele)
    
for i in range(0,n):
    sum=sum+int(lst[i])
print(sum)
