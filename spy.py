n=int(input("Enter the number: "))
s=0
p=1
while(n>0):
    d=n%10
    s+=d
    p*=d
    n//=10
if s==p:
    print("Spy number")
else:
    print("Not a spy number")