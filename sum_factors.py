n=int(input("Enter the number"))
s=0
for i in range(2,(n//2)+1):
    if n%i==0:
        s+=i
print("Sum of factors: ",s)