n=int(input("Enter the number"))
sum=0
while(n>0):
    d=n%10
    n//=10
    if d%2==0:
        sum+=d
print("The sum of even digits: ",sum)
