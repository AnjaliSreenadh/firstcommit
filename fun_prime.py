def prime(n):
    for i in range(2,n):
        f=0
        if n%i==0:
            f=1
            break
        else:
            f=0
    return f
num=int(input("Enter the number: "))
s=prime(num)
if s:
    print("Not Prime Number")
else:
    print("Prime Number")


