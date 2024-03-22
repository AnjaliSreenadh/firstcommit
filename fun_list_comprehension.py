def list_compr(l):
    n_l=[x for x in l if 's' in x]
    return n_l
n=int(input(("Enter the limit of the lsit: ")))
li=[]
print("Enter the elements")
for i in range(n):
    x=(input())
    li.append(x)
print("The list is: ",li)
new_list=list_compr(li)
print("The new list is: ",new_list)
