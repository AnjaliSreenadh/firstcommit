a=str(input("Enter"))
l=len(a)
for i in range(l):
    if i%2==0:
        print(a[i].upper(),end="")
    else:
        print(a[i].lower(),end="")
