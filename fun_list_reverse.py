def list_rev(l):
    r=[]
    for i in l:
        r=[i]+r
    print("Reverse list: ",r)
num=int(input(("Enter the limit of the list: ")))
a=[]
print("Enter the elements")
for i in range(num):
    x=int(input())
    a.append(x)
print("The list is: ",a)
list_rev(a)


