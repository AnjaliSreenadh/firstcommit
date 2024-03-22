def tuple_reverse(l):
    r=[]
    for i in lst:
        r=[i]+r
    rt=tuple(r)
    return rt

t=(1,4,10,24,5,1)
lst=list(t)
print("The tuple is: ",t)
x=tuple_reverse(lst)
print("The reversed tuple is: ",x)
