def sum_list_elts(l,n):
    sum=0
    for i in range(n):
        sum=sum+l[i]
    return sum
num=int(input("Enter the limit of the list: "))
print("Enter the elements:")
a=[]
for i in range(num):
    x=int(input())
    a.append(x)
print("Sum of the elements of the list is: ",sum_list_elts(a,num))