n=int(input("Enter the number"))
s=9
while n>0:
    d=n%10
    n//=10
    if d<s:
        s=d
print("Smallest digit is: ",s)
