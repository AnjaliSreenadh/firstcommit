n=int(input("Enter the number: "))
temp=n
rev=0
while(n>0):
    rev=(rev*10)+n%10
    n//=10
if temp==rev:
    print("The number is palindrome")
else:
    print("The number is not palindrome")