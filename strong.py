n=int(input("Enter the number: "))
temp=n
s=0
while(n>0):
    d=n%10
    f=1
    for i in range(1,d+1):
        f*=i
    n//=10
    s+=f
if temp==s:
    print("Strong number")
else:
    print("Not a strong number")