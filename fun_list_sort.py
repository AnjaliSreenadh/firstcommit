def list_sort(n,a):
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
num=int(input("Enter the limit: "))
l=[]
print("Enter the elements")
for i in range(num):
    x=int(input())
    l.append(x)
print("The list is",l)
s=list_sort(num,l)
print("The sorted list: ",s)
