def list_dupli(len,al):
    b=[]
    for i in range(len):
        if al[i] not in b:
            b.append(al[i])
    print("The list without duplicates: ",b)
l=int(input("Enter the limit: "))
a=[]
print("Enter the elements")
for i in range(l):
    x=int(input())
    a.append(x)
print("The entered list is",a)
list_dupli(l,a)
