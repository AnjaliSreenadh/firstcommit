n=int(input("Enter the limit"))
big=0
print("Enter the numbers")
for i in range(1,n+1):
  num=int(input())
  if num>big:
    big=num
print("The biggest number is: ",big)