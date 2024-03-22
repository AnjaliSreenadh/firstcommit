def list_odd_even(x,n):
    if x%2==0:
        return 1
    else:
        return 0
num=int(input("Enter the limit of the list: "))
o=[]
e=[]
print("Enter the elements")
for i in range(num):
    x=int(input())
    y=list_odd_even(x,num)
    if y:
        e.append(x)
    else:
        o.append(x)
print("Even numbers list: ",e)
print("Odd numbers list: ",o)