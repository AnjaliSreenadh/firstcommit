n=int(input("Enter the number"))
sum=0
while(n>0):
  d=n%10
  if d%2==0:
    sum+=d
  n//=10
print(sum)