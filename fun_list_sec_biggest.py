def list_sec_biggest(n,a):
    lar=0
    for i in range(n):
        if a[i]>lar:
            lar=a[i]
    sec_lar=0
    for j in range(n):
        if a[j]>=sec_lar and a[j]!=lar:
            sec_lar=a[j]
    return sec_lar
num=int(input("Enter the limit: "))
l=[]
print("Enter the elements: ")
for i in range(num):
    x=int(input())
    l.append(x)
r=list_sec_biggest(num,l)
print("The Second Biggest Element is: ",r)

