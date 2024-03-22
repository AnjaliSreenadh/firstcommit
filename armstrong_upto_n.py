n=int(input("Enter the limit"))
for i in range(1,n+1):
    l=len(str(i))
    temp=i
    s=0
    while temp>0:
        s=s+(temp%10)**l
        temp//=10
    if i==s:
        print(i)