def list_sub_check(s,sl):
    s1=set(s)
    s2=set(sl)
    i_s=s1.intersection(s2)
    if (len(i_s.symmetric_difference(s2))==0):
        return 1
    else:
        return 0
n=int(input("Enter the limit of the list: "))
a=[]
print("Enter the elements to the list")
for i in range(n):
  x=int(input())
  a.append(x)
n_s=int(input("Enter the limit of the sublist: "))
a_s=[]
print("Enter the elements to the sublist")
for i in range(n_s):
  x=int(input())
  a_s.append(x)
x=list_sub_check(a,a_s)
if x:
    print("Sublist Found")
else:
    print("Sublist Not Found")
