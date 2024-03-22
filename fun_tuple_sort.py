def tuple_sort(l):
    for i in range(len(l)):
        for j in range(0,(len(l))-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
t=(1,5,2,8,7,3,6,4,)
print("The tuple is: ",t)
a=list(t)
s_r=tuple_sort(a)
print("The sorted tuple is: ",s_r)

