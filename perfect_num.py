n=int(input("Enter the number"))
temp=n
sum=0
for i in range(1,(n//2)+1):
    if n%i==0:
        sum+=i
if sum==temp:
    print("Perfect")
else:
    print("Not a perfect  number")