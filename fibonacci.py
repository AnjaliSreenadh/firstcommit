n=int(input("Enter the limit"))
a=0
b=1
print(a)
print(b)
for i in range(1,n-1):
    print(a+b)
    a,b=b,a+b