n=int(input("enter a number"))
a=0
while(n>0):
    d=n%10
    a=a+d
    n=n//10
    
print(a)