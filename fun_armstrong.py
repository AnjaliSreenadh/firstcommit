def armstrong(n,l):
    s=0
    while(n>0):
        s=s+((n%10)**l)
        n//=10
    return s
num=int(input("Enter the number: "))
ln=len(str(num))
sum=armstrong(num,ln)
if sum==num:
    print("The number is armstrong")
else:
    print("The number is not armstrong")
